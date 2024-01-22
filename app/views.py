from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .forms import TradingSystemForm, HistoricalDataForm
from .backtester import run_backtest
from .models import TradingSystemSettings, MarketData, TradeLog, BacktestResult
main_bp = Blueprint('', __name__)
from .data_manager import get_market_data
from .historical_data_manager import download_market_data
import datetime, time

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = TradingSystemForm()
    if form.validate_on_submit():
        settings = TradingSystemSettings(
            atr_period=form.atr_period.data,
            bollinger_period=form.bollinger_period.data,
            bollinger_std_dev=form.bollinger_std_dev.data,
            risk_per_trade=form.risk_per_trade.data
        )
        db.session.add(settings)
        db.session.commit()
        run_backtest(settings)
        return redirect(url_for('results'))
    return render_template('index.html', form=form)

@main_bp.route('/results')
def results():
    results = BacktestResult.query.order_by(BacktestResult.timestamp.desc()).first()
    logs = TradeLog.query.order_by(TradeLog.timestamp.desc()).all()
    return render_template('results.html', results=results, logs=logs)

@main_bp.route('/historical-data', methods=['GET', 'POST'])
def historical_data():
    form = HistoricalDataForm()
    data = []
    if form.validate_on_submit():
        download_market_data("AAPL", '1d', '2024-01-01', '2024-01-19')
        # Here we would call a function to fetch and download the data
        # For now, we'll just redirect to the home page
        data = get_market_data()
        for datum in data:
            d = datetime.datetime.utcnow()
            datum.for_js = int(time.mktime(d.timetuple())) * 1000
        #return redirect(url_for('index'))
    return render_template('historical_data.html', form=form, data=data)