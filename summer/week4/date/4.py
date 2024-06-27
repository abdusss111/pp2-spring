from datetime import datetime, timedelta

day1 = datetime.now().replace(microsecond=0) - timedelta(days=10)
day2 = datetime.now().replace(microsecond=0)

difference = day2-day1

in_seconds = difference.total_seconds()

print(in_seconds)