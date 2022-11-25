def nCr(n, r):
    return (factorial(n) / (factorial(r)
                * factorial(n - r)))
 
def factorial(n):
    if n == 0:
        return 1
    out = 1
    for i in range(2, n+1):
        out = out * i
    return out