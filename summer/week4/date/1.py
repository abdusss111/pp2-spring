from datetime import datetime, timedelta

today = datetime.now()

minus_5 = today - timedelta(days=5)
print("today:", today)
print("minus 5 days:",minus_5)