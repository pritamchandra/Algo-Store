# gcd and lcm
def gcd(a, b):
    if a > b: a, b = b, a
    if a == 0: return b
    b, a = a, divmod(b, a)[1]
    return gcd(a, b)
    
def lcm(a, b):
    d = gcd(a, b)
    return b*int(a/d)