
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
    """Lehmer mean"""
    numpowers = [n ** p for n in numbers]
    denpowers = [n ** (p - 1) for n in numbers]
    return sum(numpowers) / sum(denpowers)


def sym_lehmer_mean(p, numbers):
    """Lehmer mean"""
    if p <= 0:
        p += 1
    return lehmer_mean(p, numbers)


def chiel_mean(numbers, integer=False):
    """Chiel mean"""
    powersums = {}
    for number in numbers:
        for prime, power in number.factor():
            try:
                powersums[prime] += power
            except KeyError:
                powersums[prime] = power

    result = 1
    n = QQ(len(numbers))
    for prime, powersum in powersums.items():
        poweravg = round(powersum / n) if integer else powersum / n
        result *= prime ** poweravg
    return result


def list_epimoric(amount=20):
    """
    This is a remarkable alternative for listing epimoric numbers.
    """
    count = 0
    numbers = [2]
    for number in numbers:
        print(number)

        a_mean = lehmer_mean(1, [1, number])
        h_mean = lehmer_mean(0, [1, number])
        numbers.append(a_mean)
        numbers.append(h_mean)

        count += 1
        if count > amount:
            break


def run():
    for number in [1, 2, 3, 4, 2 / 3, 3 / 4, 4 / 5, 5 / 6, 6 / 7, 7 / 3, 6 / 3, 9 / 4, 7 / 2, 6 / 5]:
        assert chiel_mean([1, number]) == geomean([1, number])
    # for p in range(-3, 4):
        #print('p = {}: {}'.format(p, chiel_mean(p, [1, 3/2])))

run()
