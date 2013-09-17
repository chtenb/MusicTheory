def harmonic_distance(s, t=1):
    result = 0
    weights = {2: 1, 3: 2, 5: 3}
    for p in list(factor(s / t)):
        result += weights[p[0]] * abs(p[1])
    return result


def melodic_distance(s, t=1):
    return N(abs(log(s / t) / log(2 ^ (1 / 12))))


def melodic_harmonic_distance(s, t=1, x=1, y=1):
    return N(y * harmonic_distance(s, t) + x * melodic_distance(s, t))
