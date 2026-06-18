from flask import Flask
from flask_cors import CORS
from sqlalchemy import text
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from config import Config
from db import db
from routes.commodity_routes import commodity_bp
from models.financial_series import FinancialSeries
from models.commodity_prices import CommodityPrices

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["60 per minute"]
)


app.config.from_object(Config)

app.json.sort_keys = False

CORS(app,origins=["http://localhost:3000"])

db.init_app(app)

app.register_blueprint(commodity_bp)

with app.app_context():
    try:
        result = db.session.execute(
            text("SELECT COUNT(*) FROM financial_series")
        )

        count = result.scalar()

        print(
            f"Connected! financial_series has {count} rows"
        )

    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(debug=True)