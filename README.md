# Trading System Backtester

## Overview
This project provides a web interface to backtest trend following trading systems using ATR for position sizing and Bollinger Bands for market entry signals. The backtest results are evaluated using MAR, CAGR%, and Sharpe Ratio.

## Installation
To run this project, you need to have Python installed on your system. After cloning the repository, install the required dependencies by running:

```
pip install -r requirements.txt
```

## Running the Application
To start the web application, run:

```
python run.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Configuration
The web interface allows you to configure the following attributes of the trading system:
- ATR Period
- Bollinger Bands Period
- Bollinger Bands Standard Deviation
- Risk per Trade (%)

## Backtest Results
After running a backtest, you can view the results and logs on the results page. The results include the MAR, CAGR%, and Sharpe Ratio metrics.

## Historical Data Management
The application allows you to manage a library of historical market data. You can add new data through the web interface.

## Database
The application uses SQLite to store market data, trading system settings, choices, logs, and results.

## Testing
To run the tests, use the following command:

```
pytest
```