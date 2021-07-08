from fastapi import HTTPException

from data.messageData import MessageData #getMessages, getOneMessages, saveMessages, updateMessages, deleteMessages, getMessagesByText

class MessageService:

    def getMessage():
        return MessageData.getMessages()

    def getOneMessage(channel: str):
        message = MessageData.getOneMessages(channel)
        if (len(message) == 0 ):
            raise HTTPException(status_code=404, detail="Channel not found")
        return message

    def saveMessage(message):
        existingMessage = MessageData.getMessagesByText(message.text)
        if(existingMessage):
            raise HTTPException(status_code=409, detail="Message already exists")
        return MessageData.saveMessages(message)

    def updateMessage(id, message):
        getOneMessage(message.channel)
        return MessageData.updateMessages(id, message)

    def deleteMessage(id):
        return MessageData.deleteMessages(id)