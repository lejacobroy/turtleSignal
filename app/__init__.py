from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask('app')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading_system.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    with app.app_context():
        from .views import main_bp
        app.register_blueprint(main_bp)
        db.create_all()

    return app