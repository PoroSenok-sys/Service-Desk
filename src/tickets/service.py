"""Бизнес логика для работы с tickets"""
from typing import Sequence

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from src.tickets.models import User, Ticket, Message
from src.tickets.schemas import TicketCreate, MessageCreate
from src.tickets.send_email import send_email


async def create_ticket(db: AsyncSession, ticket: TicketCreate) -> Ticket:
    user = await db.execute(select(User).where(User.email == ticket.user_email))
    user = user.scalar()
    if not user:
        user = User(email=ticket.user_email, name=ticket.user_name)
        db.add(user)
        await db.commit()
        await db.refresh(user)

    new_ticket = Ticket(user_id=user.id)
    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)

    new_message = Message(ticket_id=new_ticket.id, sender="user", content=ticket.message)
    db.add(new_message)
    await db.commit()

    await send_email(ticket.user_email, "Ваше обращение принято", "Мы начали обработку вашего обращения.")
    return new_ticket


async def get_tickets(db: AsyncSession, status: str | None = None) -> Sequence[Ticket | None]:
    query = select(Ticket).options(selectinload(Ticket.massages))
    if status:
        if status == "open" or status == "in_progress" or status == "closed":
            query = query.where(Ticket.status == status)
        else:
            raise HTTPException(status_code=404, detail="Указан некорректный статус")
    result = await db.execute(query)
    return result.scalars().all()


async def reply_to_ticket(db: AsyncSession, ticket_id: int, message: MessageCreate):
    ticket = await db.execute(select(Ticket).where(Ticket.id == ticket_id).options(joinedload(Ticket.user)))
    ticket = ticket.scalar()
    if not ticket or ticket.status == "closed":
        raise HTTPException(status_code=400, detail="Обращение не найдено или закрыто")

    new_message = Message(ticket_id=ticket_id, sender="operator", content=message.content)
    db.add(new_message)
    ticket.status = "in_progress"
    await db.commit()

    await send_email(ticket.email, "Ответ на ваше обращение", message.content)
    return {
        "status": 200,
        "message": f"Письмо отправлено клиенту по заявке с {ticket_id} id",
    }


async def close_ticket(db: AsyncSession, ticket_id: int):
    ticket = await db.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Обращение не найдено")
    ticket.status = "closed"
    await db.commit()
    await db.refresh(ticket)

    await send_email(ticket.user.email, "Обращение закрыто", "Ваше обращение успешно решено.")

    return ticket
