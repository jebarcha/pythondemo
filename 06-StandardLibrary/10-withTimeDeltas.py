# deltas = durations
from datetime import datetime, timedelta

# dt1 = datetime(2024, 1, 1)
# dt2 = datetime.now()

# duration = dt2 - dt1
# print(duration)  # 224 days, 13:23:02.020797

# print("days", duration.days)  # days 224
# print("seconds", duration.seconds)  # seconds 48261
# print("total_seconds():", duration.total_seconds())  # 19401861.092269

# ------------------
dt1 = datetime(2024, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)  # 224 days, 13:23:02.020797

print("days", duration.days)  # days 224
print("seconds", duration.seconds)  # seconds 48261
print("total_seconds():", duration.total_seconds())  # 19401861.092269
