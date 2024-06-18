import logging
from functools import wraps


logging.basicConfig(
    filename="example.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%d-%m %H:%M:%S",
)


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        logging.info(f"{func.__name__ } was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + 10


@logit
def subtraction_func(x):
    """Do some math."""
    return x - 10


@logit
def division_func(x):
    """Do some math."""
    return x / 10


result = addition_func(4)
print(result)

result2 = subtraction_func(4)
print(result2)

result3 = division_func(4)
print(result3)
