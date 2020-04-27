def fib(n):
    cur = 0
    old = 1
    i = 0
    while (i < n):
        cur, old, i = cur+old, cur, i+1
    return cur

n = 15

print("fibonacci number %d is %d" % (n, fib(n)))