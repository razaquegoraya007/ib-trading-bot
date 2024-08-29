import yfinance as yf
from ib_insync import Stock, MarketOrder, LimitOrder
import config
from stock_manager import StockManager
from trading_statistics import TradingStatistics

stock_manager = StockManager()
stats = TradingStatistics()

def fetch_market_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d")
    return hist['Close'].iloc[-1]  # Get the latest closing price

def place_order(ib, symbol, quantity, action='BUY'):
    contract = Stock(symbol, 'SMART', 'USD')
    order = MarketOrder(action, quantity)
    trade = ib.placeOrder(contract, order)
    return trade

def execute_strategy(ib):
    stocks = stock_manager.get_stocks()
    print(f"Current stocks: {stocks}")
    for symbol, stock_info in stocks.items():
        print(f"Processing symbol: {symbol}")
        print(f"Stock info: {stock_info}")

        price = fetch_market_data(symbol)
        print(f"Fetched market data for {symbol}: {price}")

        base_shares = stock_info['base_shares']
        buy_threshold = stock_info['buy_threshold']
        take_profit_percentage = stock_info['take_profit_percentage']
        max_downtrend_purchases = stock_info['max_downtrend_purchases']
        purchases_count = stock_info['purchases_count']

        target_price = price * (1 - buy_threshold)
        print(f"Target buy price for {symbol}: {target_price}")

        if purchases_count < max_downtrend_purchases:
            if price <= target_price:
                print(f"Buying {base_shares} shares of {symbol} at {price}")
                trade = place_order(ib, symbol, base_shares, 'BUY')
                take_profit_price = price * (1 + take_profit_percentage)
                print(f"Placing TAKE PROFIT order for {symbol} at {take_profit_price}")
                take_profit_order = LimitOrder('SELL', base_shares, take_profit_price)
                ib.placeOrder(trade.contract, take_profit_order)
                stock_manager.update_stock(symbol, purchases_count=purchases_count + 1)
                stats.record_trade(profit=take_profit_percentage)
            else:
                print(f"No purchase for {symbol}, price not low enough.")
        else:
            print(f"Max downtrend purchases reached for {symbol}.")
