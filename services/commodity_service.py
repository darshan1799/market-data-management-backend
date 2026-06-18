from models.financial_series import FinancialSeries

def get_commodities_by_type(interval_type):

    series = FinancialSeries.query.filter_by(
        interval_type=interval_type
    ).first()

    if not series:
        return None

    return {
        "id": series.id,
        "name": series.name,
        "interval_type": series.interval_type,
        "unit": series.unit,
        "data": [
            {
                "date": price.record_date.isoformat(),
                "value": float(price.value)
            }
            for price in series.prices
        ]
    }