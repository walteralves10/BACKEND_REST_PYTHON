from fastapi import APIRouter, status

from data.messageData import Message
from service.messageService import MessageService #getMessage, getOneMessage, saveMessage, updateMessage, deleteMessage

message = APIRouter()

@message.get("/channels")
def get_channels():
    return MessageService.getMessage() 

@message.get("/message/{channel}")
def get_message(channel: str):
    return MessageService.getOneMessage(channel)

@message.post("/message", status_code=status.HTTP_201_CREATED)
def create_message(message: Message):
    return MessageService.saveMessage(message) 

@message.put("/message/{id}", status_code=204)
def update_message(id: str, message: Message):
    return MessageService.updateMessage(id, message) 

@message.delete("/message/{id}", status_code=204)
def delete_message(id: str):
    return MessageService.deleteMessage(id)