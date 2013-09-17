# A shouldn't contain 1
# Returns generator of approximation tonality


def approximate(A, delta):
    # filter 1 and replace a < 1 with 1/a
    a = A[0]
    x = a * delta
    while True:
        a, n = getNonCoveredTone(A, x, delta)
        if a == None:
            return x
#        print "n", n
#        print "x", x
#        print "x^n", x ^ n
#        print "a", a
        d = (x ^ n / (delta * a)) ^ (1 / n) + \
            0.00001  # cheat for rounding error
#        print "d", d
        x = x / d


def getNonCoveredTone(A, x, delta):
    for a in A:
        n = 0
        while True:
            n += 1
            # If a is covered, break
            if delta ^ -1 * a <= x ^ n and x ^ n <= delta * a:
                break
            # If not covered, return upper bound
            if x ^ n > delta * a:
                # print "n", n
                # print "x", x
                # print "a", a
                # print "x^n", x ^ n
                # print "delta * a", delta * a
                # print x ^ n > delta * a
                # y = float(float(x) ^ float(n))
                # z = float(float(delta) * float(a))
                # print "y", y
                # print "z", z
                # print y > z
                # print y == z
                return a, n
    return None, None

delta = 1.01
Zarlino = [3 ^ 2 / 2 ^ 3, 5 / 2 ^ 2,
           2 ^ 2 / 3, 3 / 2, 5 / 3, (3 * 5) / 2 ^ 3, 2]
print approximate(Zarlino, delta)
