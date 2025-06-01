import sys

def is_increasing(n: int):
    if n < 10:
        return True
    ultim = n % 10
    penúltim = (n // 10) % 10
    if ultim >= penúltim:
        return is_increasing(n//10)         
    else: 
        return False
    


for line in sys.stdin:
    n = int(line)
    print(str(is_increasing(n)).lower())