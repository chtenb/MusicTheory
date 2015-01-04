
def geomean(numbers):
    """Geometric mean"""
    product = 1
    for n in numbers:
        product *= n
    return pow(product, 1 / len(numbers))


def p_mean(p, numbers):
    """Power mean"""
    if p == 0:
        return geomean(numbers)

    powers = [n ** p for n in numbers]
    return (sum(powers) / len(numbers)) ** (1 / p)


def lehmer_mean(p, numbers):
    """Power mean"""
    if p == 0:
        return geomean(numbers)

    numpowers = [n ** p for n in numbers]
    denpowers = [n ** (p - 1) for n in numbers]
    return sum(numpowers) / sum(denpowers)


for p in range(-9, 10):
    print('p = {}: {}'.format(p, lehmer_mean(p, [1, 2])))
