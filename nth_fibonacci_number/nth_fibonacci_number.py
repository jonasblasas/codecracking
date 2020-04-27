def fib(n):
    cur = 1
    old = 1
    i = 1
    while (i < n):
        cur, old, i = cur+old, cur, i+1
    return cur

n = 100

print("fibonacci number %d is %d" % (n, fib(n)))