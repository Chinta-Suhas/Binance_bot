from bot.client import BinanceFuturesClient
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def create_order(self, symbol, side, order_type, quantity, price=None):
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        order = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            order["price"] = price
            order["timeInForce"] = "GTC"

        return self.client.place_order(**order)
