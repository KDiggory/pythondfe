def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

test = is_prime(5)
print(f"Is the numnber 5 a prime? {test}")

test2 = is_prime(6)
print(f"Is the numnber 6 a prime? {test2}")

test3 = is_prime(25)
print(f"Is the numnber 25 a prime? {test3}")