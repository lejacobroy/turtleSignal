from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class TradingSystemForm(FlaskForm):
    atr_period = IntegerField('ATR Period', validators=[DataRequired(), NumberRange(min=1)])
    bollinger_period = IntegerField('Bollinger Bands Period', validators=[DataRequired(), NumberRange(min=1)])
    bollinger_std_dev = FloatField('Bollinger Bands Std Dev', validators=[DataRequired(), NumberRange(min=0.1)])
    risk_per_trade = FloatField('Risk per Trade (%)', validators=[DataRequired(), NumberRange(min=0.1, max=100)])
    submit = SubmitField('Run Backtest')