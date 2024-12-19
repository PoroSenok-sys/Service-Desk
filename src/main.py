"""Основной файл запуска"""
import os
import sys

from fastapi import FastAPI

from src.tickets.router import router as router_tickets


sys.path.insert(1, os.path.join(sys.path[0], '..'))


app = FastAPI(
    title="Service Desk"
)

app.include_router(router_tickets)
