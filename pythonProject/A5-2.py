# Hamin Han XK26538

# Q6

def is_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

primes = (x for x in range(2,100) if is_prime(x))
print(primes)
print(list(primes))

# Q7

def factor_gen(n):
    ''' generates the prime factors of the input number n '''
    if n <= 3:
        raise Exception ("n should be a positive int greater than 3")
    else:
        num = n
        traverse = 2
        while num != 1:
            if num % traverse == 0:
                num = num / traverse
                yield traverse
            else:
                traverse += 1
                while not is_prime(traverse):
                    traverse += 1

factors_51 = factor_gen(51)
print(factors_51)
print(sorted(list(factors_51)))

factors_18000 = factor_gen(18000)
print(factors_18000)
print(sorted(list(factors_18000)))

factors_16 = factor_gen(16)
print(factors_16)
print(sorted(list(factors_16)))

factors_625 = factor_gen(625)
print(factors_625)
print(sorted(list(factors_625)))

factors_753 = factor_gen(753)
print(factors_753)
print(sorted(list(factors_753)))

# Q8

import random

def random_gen(m, n):
    ''' generates m random integer numbers between 0 and n '''
    repeat = m
    while m != 0:
        ran = random.randint(0,n)
        m -= 1
        print("Next random score is: %d" % ran)
        yield ran


def converter_gen(scores):
    ''' converts the numeric scores to letter grades '''
    for num in scores:
        if num >= 0 and num <= 59:
            yield 'F'
        if num >= 60 and num <= 69:
            yield 'D'
        if num >= 70 and num <= 79:
            yield 'C'
        if num >= 80 and num <= 89:
            yield 'B'
        if num >= 90 and num <= 100:
            yield 'A'

random_grades = converter_gen(random_gen(5, 100))
print(random_grades)
print(list(random_grades))