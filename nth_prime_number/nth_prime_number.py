import math

def prime(n):
    start = 2
    count = 0
    while True:
        if all([start % i for i in range(2, int(math.sqrt(start)) +1)]) != 0:
            count += 1
            if count == n:
                return start
        start += 1

n = 1000
print("prime number %d is %d" % (n, prime(n)))