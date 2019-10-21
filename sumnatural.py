

def generator(limit):
    sum = 0
    tocheck  = [number for number in range(limit) if number % 3 == 0 or number % 5 == 0]

    for number in tocheck:
        sum = sum + number
    return sum

print(generator(10))