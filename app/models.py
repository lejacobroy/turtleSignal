from . import db
from sqlalchemy import func

class MarketData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)

class TradingSystemSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atr_period = db.Column(db.Integer, nullable=False)
    bollinger_period = db.Column(db.Integer, nullable=False)
    bollinger_std_dev = db.Column(db.Float, nullable=False)
    risk_per_trade = db.Column(db.Float, nullable=False)

class TradeLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=func.now())
    action = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    atr_value = db.Column(db.Float, nullable=False)
    position_size = db.Column(db.Float, nullable=False)

class BacktestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=func.now())
    mar = db.Column(db.Float, nullable=False)
    cagr = db.Column(db.Float, nullable=False)
    sharpe_ratio = db.Column(db.Float, nullable=False)