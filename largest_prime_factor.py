# lpf(n) : largest prime factor of n
def lpf(n):
    for div in range(2, int(sqrt(n)) + 1):
        if n%div == 0:
            return max(div, lpf(int(n/div)))
    
    return n