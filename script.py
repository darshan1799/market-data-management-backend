# import requests
# from db import db
# from models.financial_series import FinancialSeries
# from models.commodity_prices import CommodityPrices
# from app import app

# def fetch_commodities(interval):
#     api_key = "demo" 

#     url = (
#         f"https://www.alphavantage.co/query"
#         f"?function=ALL_COMMODITIES"
#         f"&interval={interval}"
#         f"&apikey={api_key}"
#     )

#     response = requests.get(url)
#     response.raise_for_status()

#     return response.json()

# def save_commodities(interval):
#     payload = fetch_commodities(interval)

#     series = FinancialSeries(
#         name=payload["name"],
#         interval_type=payload["interval"],
#         unit=payload["unit"]
#     )

#     db.session.add(series)
#     db.session.flush()  # gets id without commit

#     prices = [
#         CommodityPrices(
#             financial_series_id=series.id,
#             record_date=item["date"],
#             value=item["value"]
#         )
#         for item in payload["data"]
#     ]

#     db.session.bulk_save_objects(prices)
#     db.session.commit()

# with app.app_context():
#     save_commodities("annual")  
