def factorial_iter(n):
    result=1
    for i in range(2, n+1):
        result *=i
        return result
def factorial_rec(n):
    return 1 if n<=1 else n*factorial_rec(n-1)
print(factorial_iter(5))
print(factorial_rec(6))
