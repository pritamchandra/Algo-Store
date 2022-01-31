# number of factors of n
def count_factors(n, two_power = 1):
    if n%2 == 0:
        return count_factors(int(n/2), two_power + 1)
    
    m, count = sqrt(n), 0
    for div in range(1, ceil(m), 2):
        if n%div == 0: count += 2
            
    if m == int(m): count += 1
        
    return count*two_power