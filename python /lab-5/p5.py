def prime_factors(n):
    factors = []
    if n % 2 == 0:
        while n % 2 == 0:
            factors += [2]
            n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            while n % i == 0:
                factors += [i]
                n //= i
    if n > 2:
        factors += [n]
    return factors

n = int(input("Enter a number: "))
factors = prime_factors(n)

print("The prime factors of", n, "are:", factors)