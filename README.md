# Binance Futures Testnet Trading Bot

## Setup
1. Create Binance Futures Testnet account
2. Generate API keys
3. Create `.env` file with:
   - BINANCE_API_KEY
   - BINANCE_API_SECRET
4. Install dependencies:
   pip install -r requirements.txt

## Run
MARKET:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

## Assumptions
- USDT-M Futures only
- Testnet environment
- Single order per CLI execution
