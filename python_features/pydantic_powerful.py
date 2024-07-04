from pydantic import BaseModel, field_validator
import datetime as dt


class Order(BaseModel):
    id: int
    created_at: dt.datetime
    status: str
    price: float
    quantity: int
    symbol: str
    side: str

    class Config:
        validate_assignment = True

    @field_validator("quantity")
    def validate_quantity(cls, value):
        if not isinstance(value, int):
            raise ValueError("Quantity must be an integer")
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        return value

    @field_validator("created_at")
    def validate_created_at(cls, value):
        if value > dt.datetime.now():
            raise ValueError("Created_at cannot be in the future")
        return value


if __name__ == "__main__":
    order = Order(
        id=1,
        created_at=dt.datetime.now(),
        status="open",
        price=100.0,
        quantity=10,
        symbol="AAPL",
        side="buy",
    )
    print(order)
