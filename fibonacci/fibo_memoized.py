## Python program for fibonacci memoized version
fibo_cache = {}

def fibo_memo(n):
    if n in fibo_cache:
        return fibo_cache[n]
    else:
        fibo_cache[n] = n if n < 2 else fibo_memo(n-2) + fibo_memo(n-1)
        return fibo_cache[n]

print(fibo_memo(9))

