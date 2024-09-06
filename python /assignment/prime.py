def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

count = 0
current_number = 2
primes_per_row = 10

while count < 50:
    if is_prime(current_number):
        print(f"{current_number:4}", end=' ')
        count += 1
        if count % primes_per_row == 0:
            print()
    current_number += 1