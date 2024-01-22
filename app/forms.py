from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, NumberRange

class HistoricalDataForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField('End Date', validators=[DataRequired()], format='%Y-%m-%d')
    timeframe = SelectField('Timeframe', choices=[('1D', '1 Day'), ('1W', '1 Week'), ('1M', '1 Month')], validators=[DataRequired()])
    submit = SubmitField('Download')

class TradingSystemForm(FlaskForm):
    atr_period = IntegerField('ATR Period', validators=[DataRequired(), NumberRange(min=1)])
    bollinger_period = IntegerField('Bollinger Bands Period', validators=[DataRequired(), NumberRange(min=1)])
    bollinger_std_dev = FloatField('Bollinger Bands Std Dev', validators=[DataRequired(), NumberRange(min=0.1)])
    risk_per_trade = FloatField('Risk per Trade (%)', validators=[DataRequired(), NumberRange(min=0.1, max=100)])
    submit = SubmitField('Run Backtest')