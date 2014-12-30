# Compute combinations of 3 and 5 powers,
# and make them be in [1,2] using powers of 2


def getPureTones(position):
    # Hardcoded approach
    Zarlino = [1 * 2 ^ 0, 3 ^ 2 / 2 ^ 3 * 2 ^ 0, 5 / 2 ^ 2 * 2 ^ 0, 2 ^ 2 / 3 * 2 ^ 0, 3 / 2 * 2 ^ 0, 5 / 3 * 2 ^ 0, (3 * 5) / 2 ^ 3 * 2 ^ 0]
    points = []
    for n in Zarlino:
        points.append(
            point((n, position), rgbcolor=(1, 0, 0), pointsize=25))
    return points

    # Dynamic approach
    powersOf3 = [pow(3, p) for p in [-3..3]]
    powersOf5 = [pow(5, p) for p in [-3..3]]
    powersOf7 = [pow(7, p) for p in [-3..3]]

    result = [p * q * r
              for p in powersOf3
              for q in powersOf5
              for r in powersOf7] + [2]

    def mod2(n):
        while(n < 1 or n > 2):
            if (n < 1):
                n *= 2
            if (n > 2):
                n /= 2
        return n

    resultMod2 = [mod2(n) for n in result]
    # The treshold for the to be considered pure tones
    cTreshold = 20
    resultFiltered = filter(lambda n: c([1, n]) <= cTreshold, resultMod2)
    resultPoints = []
    for n in resultFiltered:
        rColor = c([1, n]) / cTreshold
        resultPoints.append(
            point((n, position), rgbcolor=(rColor, 1 - rColor, 0)))
    return resultPoints


# Eulers agreeableness
# h is a harmony, that is, a list of tones,
# each represented by a natural number
def agr(h):
    result = 1
    # print "factor(lcm(h)): "+str(factor(lcm(h)))
    for (g, p) in factor(lcm(h)):
        result += (g - 1) * p
    return result


# The complexity is Eulers agreeableness applied to any rational
# harmony h
def c(h):
    for i in range(len(h)):
        d = denominator(Rational(h[i]))
        for j in range(len(h)):
            h[j] *= d
    for i in range(len(h)):
        h[i] = floor(h[i])
    return agr(h)
