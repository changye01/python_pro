def gcd(m, n):
    if n == 0:
        return m
    r = m % n
    return(gcd(n, r))


sx = gcd(10, 2)
print(sx)
