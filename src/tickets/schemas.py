"""Схемы для работы с tickets"""
from datetime import datetime
from typing import List

from pydantic import BaseModel, EmailStr


class MessageBase(BaseModel):
    sender: str
    content: str


class MessageCreate(BaseModel):
    content: str


class MessageResponse(MessageBase):
    id: int
    created_at: datetime


class TicketCreate(BaseModel):
    user_email: EmailStr
    user_name: str
    message: str


class TicketResponse(BaseModel):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime
    messages: List[MessageResponse]  # Вложенные сообщения
