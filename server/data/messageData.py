from pydantic import BaseModel
from bson.objectid import ObjectId

from infra.database import conn

#Classe Menssagem definida por Pydantic
class Message(BaseModel):
    channel: str
    author: str
    text: str 

class MessageData:

    def messageEntity(item) -> dict:
        return {
            "id":str(item["_id"]),
            "channel":item["channel"],
            "author":item["author"],
            "text":item["text"]
        }

    def messagesEntity(entity) -> list:
        return [MessageData.messageEntity(item) for item in entity]
    # --------------------------------------------------------

    def getMessages():
        return conn.slack.message.distinct("channel")

    def getOneMessages(channel: str):
        return MessageData.messagesEntity(conn.slack.message.find({"channel": channel}))

    def getMessagesByText(text: str):
        return MessageData.messagesEntity(conn.slack.message.find({"text": text}))

    def saveMessages(message):
        conn.slack.message.insert_one(message.dict())
        return MessageData.messagesEntity(conn.slack.message.find())

    def updateMessages(id, message):
        conn.slack.message.update_one({"_id": ObjectId(id)}, {"$set": message.dict()})
        return MessageData.messageEntity(conn.slack.message.find_one({"_id": ObjectId(id)}))

    def deleteMessages(id):
        conn.slack.message.delete_one({"_id": ObjectId(id)})
        return conn.slack.message.find_one({"_id": ObjectId(id)})