import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET"),
            testnet=True  # Use testnet instead of setting FUTURES_URL
        )

    def place_order(self, **kwargs):
        try:
            logger.info(f"Placing order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            error_msg = str(e)
            logger.exception(f"API error: {error_msg}")
            raise Exception(f"Order failed: {error_msg}") from e
