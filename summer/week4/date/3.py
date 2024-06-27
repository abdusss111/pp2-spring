from datetime import datetime, timedelta

today = datetime.now()
print(today)

today = today.replace(microsecond=0)
print(today)
