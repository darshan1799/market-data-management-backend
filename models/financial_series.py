from db import db
from sqlalchemy.sql import func

class FinancialSeries(db.Model):

    __tablename__ = "financial_series"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=False)

    interval_type = db.Column(db.String(50), nullable=False)

    unit = db.Column(db.String(255), nullable=False)

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )

    prices = db.relationship(
        "CommodityPrices",
        backref="financial_series",
        lazy=True
    )