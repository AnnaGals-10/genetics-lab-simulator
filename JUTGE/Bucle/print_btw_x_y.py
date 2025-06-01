def print_btw_x_y(x,y):
    if x==y:
        print(x)
    if x>y:
        while x!=y:
            print(x)
            x-=1
        print(y)
    if y>x:
        while y!=x:
            print(y)
            y-=1
        print(x)


x, y = map(int, input().split())
print_btw_x_y(x, y)