from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .forms import TradingSystemForm
from .backtester import run_backtest
from .models import TradingSystemSettings, MarketData, TradeLog, BacktestResult
main_bp = Blueprint('', __name__)

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