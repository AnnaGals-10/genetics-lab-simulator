import heapq as cp

item = pytokr()
n = int(item())
q = [float(item()) for _ in range(n)]

cp.heapify(q)

res = 0
while len(q) > 1:
    x = cp.heappop(q)
    y = cp.heappop(q)
    cp.heappush(q,x + y) 
    res += (x + y)

print("expected number of bits per letter: %.4f" % (res / 100))