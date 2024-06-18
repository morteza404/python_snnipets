import uvicorn
from fastapi import FastAPI
from aio_pika import connect_robust, Message

app = FastAPI()
rabbitmq_url = "amqp://morteza:1@localhost/"


@app.post("/publish")
async def publish_message(message: str):
    connection = await connect_robust(rabbitmq_url)
    channel = await connection.channel()
    await channel.default_exchange.publish(
        Message(body=message.encode()), routing_key="my_queue"
    )
    await connection.close()
    return {"message": "Message published successfully!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8010)