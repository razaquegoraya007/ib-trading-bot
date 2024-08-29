# Configuration parameters for the trading bot

# General configuration
BUY_PWR_THRESHOLD = 10000  # The bot will stop buying when buying power is <= $10,000
EX_LIQ_THRESHOLD = 5000    # The bot will stop buying when excess liquidity is <= $5,000

# Stock-specific parameters (can be adjusted as needed)
STOCKS = {
    'AAPL': {
        'base_shares': 10,
        'buy_threshold': 0.01,  # Lowered to 1% for testing
        'take_profit_percentage': 0.10,
        'max_downtrend_purchases': 3,
        'purchases_count': 0
    },
    'GOOG': {
        'base_shares': 5,
        'buy_threshold': 0.01,  # Lowered to 1% for testing
        'take_profit_percentage': 0.10,
        'max_downtrend_purchases': 3,
        'purchases_count': 0
    },
}

# Additional settings
LOGGING_LEVEL = 'INFO'  # Logging level, can be set to DEBUG, INFO, WARNING, ERROR, CRITICAL

