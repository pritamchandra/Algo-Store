# The N-th prime number
def prime_number(N):
    Primes = [2]
    count, n = 1, 3

    while count < N:
        is_prime_n = True
        for prime in Primes:
            if prime > sqrt(n): 
                break
            if n % prime == 0:
                is_prime_n = False
                break

        if is_prime_n:
            Primes.append(n)
            count += 1
        
        n += 1
        
    return Primes[-1]