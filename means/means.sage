def arithmean(*numbers):
    """Arithmetical mean"""
    return sum(numbers) / len(numbers)


def geomean(*numbers):
    """Geometric mean"""
    product = 1
    for n in numbers:
        product *= n
    return pow(product, 1 / len(numbers))


def harmonicmean(*numbers):
    """Harmonic mean"""
    reciprocals = [1 / n for n in numbers]
    return len(numbers) / sum(reciprocals)


def quadraticmean(*numbers):
    """Quadratic mean"""
    squares = [n ** 2 for n in numbers]
    return sqrt(sum(numbers) / len(numbers))


def quadratic_harmonicmean(*numbers):
    """Quadratic mean"""
    square_reciprocals = [1 / n ** 2 for n in numbers]
    return len(numbers) / sum(square_reciprocals) ** 2


print(arithmean(1, 2))
print(geomean(1, 2))
print(harmonicmean(1, 2))
print(quadraticmean(1, 2))
print(quadratic_harmonicmean(1, 2))

