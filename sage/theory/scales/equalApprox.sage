# Compute combinations of 3 and 5 powers,
# and make them be in [1,2] using powers of 2


def getEqualApprox(n, position):
    resultPoints = [point((pow(2, i / n), position), pointsize=25) for i in [0..n]]
    return resultPoints
