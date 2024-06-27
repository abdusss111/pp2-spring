from datetime import datetime, timedelta

today = datetime.now()

print(today - timedelta(days=1), today, today + timedelta(days=1), sep='\n')
