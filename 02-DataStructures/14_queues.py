from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
removed = queue.popleft()
print(removed)
print(queue)  # deque([2, 3])

# if queue is empty
if not queue:
    print("empty queue")
