def multiply(a, b):
    result = 0
    positive = abs(b)
    for _ in range(positive):
        # ternary operator
        result = result + a if (positive == b) else result - a
    return result


print(f"2 * 3 = {multiply(2, 3)}")
print(f"-2 * 3 = {multiply(-2, 3)}")
print(f"2 * -3 = {multiply(2, -3)}")
print(f"-2 * -3 = {multiply(-2, -3)}")
print(f"2 * 0 = {multiply(2, 0)}")
