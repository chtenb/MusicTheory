#!/usr/bin/env sage -python

import sys
from sage.all import *

#eulers agreeableness
#h is a harmony, that is, a list of tones, each represented by a natural number
def agr(h):
	result = 1
	#print "factor(lcm(h)): "+str(factor(lcm(h)))
	for (g,p) in factor(lcm(h)):
		result += (g-1)*p
	return result

def cInterval(a,b):
	ratio = Rational(b) / Rational(a)
	result = 1
	f = list(factor(numerator(ratio))) + list(factor(denominator(ratio)))
	print f
	for (g,p) in f:
        	result += (g-1)*p
	return result

def c(h):
	for i in range(0,len(h)):
		d = denominator(Rational(h[i]))
		for j in range(0,len(h)):
			h[j] *=  d
	for i in range(0,len(h)):
		h[i] = floor(h[i])
	return agr(h)
