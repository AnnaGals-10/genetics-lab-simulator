def temps(n):
    h = (n // 3600)
    m = (n % 3600) // 60
    s = (n % 60)
    return h, m, s

n = int(input())
h, m, s = temps(n)
print(h, m, s)

