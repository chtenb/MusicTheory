
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
    numpowers = [n ** p for n in numbers]
    denpowers = [n ** (p - 1) for n in numbers]
    return sum(numpowers) / sum(denpowers)


def list_epimoric(amount=20):
    """This is a remarkable alternative for listing epimoric numbers."""
    count = 0
    numbers = [2]
    for number in numbers:
        a_mean = lehmer_mean(1, [1, number])
        h_mean = lehmer_mean(0, [1, number])
        numbers.append(a_mean)
        numbers.append(h_mean)

        print(number)
        count += 1
        if count > amount:
            break

list_epimoric()
#print('p = {}: {}'.format(p, lehmer_mean(p, [1, 5/4])))
