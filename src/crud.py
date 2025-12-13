from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel

app = FastAPI()
class MessageCreate(BaseModel):
    content : str
class Message(BaseModel):
    id : int
    content : str

messages_db:list[Message] = [Message(id=0, content="First post")]

@app.get("/messages",response_model=list[Message])
async def read_messages() -> list[Message]:
    return messages_db

@app.get("/messages/{message_id}",response_model=Message)
async def read_the_message(message_id : int):
    for message in messages_db:
        if message.id == message_id:
            return message
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Message not found")

@app.post("/messages",response_model=Message,status_code=status.HTTP_201_CREATED)
async def create_the_message(message:MessageCreate) -> Message:
    next_id = max((msg.id for msg in messages_db),default = 1) + 1
    new_messsage = Message(id=next_id, content=message.content)
    messages_db.append(new_messsage)
    return new_messsage

@app.put("/messages/{message_id}",response_model=Message)
async def update_message(message_id : int,message_create:MessageCreate) -> Message:
    for i,message in enumerate(messages_db):
        if message.id == message_id:
            updated_message = Message(id=message.id,content=message_create.content)
            messages_db[i] = updated_message
            return updated_message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Message not found")

@app.delete("/messages/{message_id}", status_code=status.HTTP_200_OK)
async def delete_message(message_id: int) -> dict:
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            messages_db.pop(i)
            return {"detail": f"Message ID={message_id} deleted!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

@app.delete("/messages", status_code=status.HTTP_200_OK)
async def delete_messages() -> dict:
    messages_db.clear()
    return {"detail": "All messages deleted!"}
