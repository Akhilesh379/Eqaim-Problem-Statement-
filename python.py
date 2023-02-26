def count_valid_numbers():
    count = 0

    # loop through all possible two-digit and three-digit numbers
    for i in range(10, 100):
        if i % 10 > i // 10:
            count += 1

    for i in range(100, 1000):
        if i % 10 > i // 10 % 10 > i // 100:
            count += 1

    # return the count of valid numbers
    return count

# example usage
print(count_valid_numbers())
