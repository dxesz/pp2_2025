def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

print(filter_prime([10, 15, 3, 5, 7, 9, 11, 13]))  # [3, 5, 7, 11, 13]

import math

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius**3

print(sphere_volume(3))
