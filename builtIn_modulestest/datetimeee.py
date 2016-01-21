from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)
print(now + timedelta(hours=26))
haha = datetime.utcnow().replace(tzinfo=timezone.utc)
print(haha)
