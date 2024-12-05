from fastapi import FastAPI, HTTPException
import uvicorn
import pika
import json

app = FastAPI()

def publish_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='message_queue')
    channel.basic_publish(exchange='', routing_key='message_queue', body=json.dumps(message))
    connection.close()

@app.post("/submit/")
async def submit_message(message: dict):
    if "message" not in message or "alias" not in message:
        raise HTTPException(status_code=400, detail="Invalid payload")
    publish_message(message)
    return {"status_code": 200}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)