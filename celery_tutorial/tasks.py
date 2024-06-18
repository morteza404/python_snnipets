from celery import Celery

# Create a Celery instance
app = Celery(
    "myapp", broker="amqp://guest:guest@localhost:5672/", backend="rpc://"
)  # RabbitMQ as the result backend


# Define a task
@app.task
def add(x, y):
    return x + y
