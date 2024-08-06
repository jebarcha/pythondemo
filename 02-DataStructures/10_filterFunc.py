items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# filtered = filter(lambda item: item[1] >= 10, items) #result a filter object: <filter object at 0x000001DCFB6A9B70>
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)  # [('Product1', 10), ('Product3', 12)]
