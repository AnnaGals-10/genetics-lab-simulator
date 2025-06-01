def max_de_tres(a,b,c):
    if a>=b and a>=c:
        return a
    if b>=a and b>=c:
        return b
    else:
        return c
    
a, b, c = map(int, input().split())
print(max_de_tres(a,b,c))