def doFib(n):
    fib = {}

    for k in range (1, n + 1):
        if k <= 2: f = 1
        else: f = fib[k-1] + fib[k-2]
        fib[k] = f
    return fib[n]

def badFib(n):
    if n <= 2: f = 1
    else: f = badFib(n-1) + badFib(n-2)
    return f

print(badFib(50))