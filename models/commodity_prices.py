from db import db
from sqlalchemy.sql import func

class CommodityPrices(db.Model):

    __tablename__ = "commodity_prices"

    id = db.Column(db.Integer, primary_key=True)

    financial_series_id = db.Column(
        db.Integer,
        db.ForeignKey("financial_series.id"),
        nullable=False
    )

    record_date = db.Column(
        db.Date,
        nullable=False
    )

    value = db.Column(
        db.Numeric(15, 6)
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )