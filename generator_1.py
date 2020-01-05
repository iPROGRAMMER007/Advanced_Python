import sys

def calulate_square(n):
    result = []

    for x1 in range(n):
        result.append(x1**2)

    return result

print(calulate_square(10))

print(sys.getsizeof(calulate_square(10000)))

print("*"*50)

def calculate_squareG(n):

    for x2 in range(n):
        yield x2**2


for x in calculate_squareG(10):
    print(x)

print(sys.getsizeof(calculate_squareG(10000)))


