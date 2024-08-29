from ib_connection import IBConnection
from strategy import execute_strategy
from trading_statistics import TradingStatistics

def main():
    print("Starting main.py")
    ib = IBConnection()
    if ib.connect():
        print("Connected to IB API")
        print("Starting strategy execution...")
        execute_strategy(ib)
        print("Strategy execution completed.")
        stats = TradingStatistics()
        print("Trading Statistics:", stats.get_stats())
    else:
        print("Failed to connect to IB API")
    print("Finished main.py")

if __name__ == '__main__':
    main()
