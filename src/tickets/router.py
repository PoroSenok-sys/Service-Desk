"""Эндпоинты для работы с tickets"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.tickets.schemas import TicketCreate, MessageCreate
from src.tickets.service import create_ticket, get_tickets, reply_to_ticket, close_ticket
from src.database import get_db

router = APIRouter(
    prefix="/desk",
    tags=["Service Desk"]
)


@router.get("/")
async def list_tickets(status: str | None = None, db: AsyncSession = Depends(get_db)):
    """
    Эндпоинт для просмотра списка обращений и связанных с ними сообщений
    """
    return await get_tickets(db, status=status)


@router.post("/")
async def create_new_ticket(ticket: TicketCreate, db: AsyncSession = Depends(get_db)):
    """
    Эндпоинт для создания обращения, вместе с которым в БД создается запись клиента,
    если таковой не было ранее, отправляется письмо клиенту с уведомнелием и
    создается сообщение от клиента привязанное к этому обращению
    """
    return await create_ticket(db, ticket)


@router.post("/{ticket_id}/reply")
async def reply(ticket_id: int, message: MessageCreate, db: AsyncSession = Depends(get_db)):
    """
    Эндпоинт для обработки обращения и формирование письма для ответа клиенту
    """
    return await reply_to_ticket(db, ticket_id, message)


@router.post("/{ticket_id}/close")
async def close(ticket_id: int, db: AsyncSession = Depends(get_db)):
    """
    Эндпоинт для закрытия обращения и уведомления клиента об этом через почту
    """
    return await close_ticket(db, ticket_id)
