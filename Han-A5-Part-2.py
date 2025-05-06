# Hamin Han XK26538

# Q6

def is_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

primes = (x if is_prime(x) for x in range(2,100))
print(primes)
print(list(primes))

# Q7


# Q8
