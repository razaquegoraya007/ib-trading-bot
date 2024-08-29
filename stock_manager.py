import config

class StockManager:
    def __init__(self):
        self.stocks = config.STOCKS

    def get_stocks(self):
        return self.stocks

    def update_stock(self, symbol, purchases_count):
        if symbol in self.stocks:
            self.stocks[symbol]['purchases_count'] = purchases_count
