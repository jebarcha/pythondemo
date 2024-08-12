import time

# print(time.time()) # 1723489880.131387


def send_emails():
    for i in range(100000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
