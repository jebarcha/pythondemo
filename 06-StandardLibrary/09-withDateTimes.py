from datetime import datetime
import time

dt = datetime(2024, 1, 1)
print(dt)  # 2024-01-01 00:00:00
dtNow = datetime.now()  # 2024-08-12 13:15:04.495462

# datetime.strptime  # parsing or converting a date time string
dt = datetime.strptime("2024/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)  # 2024-08-12 13:17:55.048932

print(f"{dt.year}/{dt.month}")  # 2024/8
dt.strftime("#Y/%m")  # opposite of strptime

print(dt > dtNow)  # True
