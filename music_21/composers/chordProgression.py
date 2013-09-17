from music21 import *
from rational import *
import random
import euler
from inverse import *
import copy


def genChordProgression(nrOfChords):
	s = stream.Stream()
	h = [4,5,6]
	primes = [3,5,1.0/5,1.0/3]
	for i in range(0,nrOfChords):
		while True:
			pos = random.randint(0,2)
			primeCount = random.randint(1,1)
			factor = 1
			for j in range(0,primeCount):
				factor *= primes[random.randint(0,len(primes)-1)]
			result = h[:]
			result[pos] *= factor
			#if (euler.c(result + [1]) < 14):
			agr = euler.c(result) 
			if (agr < 12):
				h = result
				s.append(HertzToChord(h))
				break
	return s

theme1 = genChordProgression(8)
for thingy in theme1.flat:
	theme1.append(thingy)
theme1.show()
exit()
#theme1.append(copy.deepcopy(theme1))
theme2 = inverse(theme1, 'c4')
theme1.append(theme2)

theme2.show()
