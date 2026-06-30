y = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x, "is even")
        y = y + 1
print(f"Number of {y} even numbers:", y)
