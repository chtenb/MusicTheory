from music21 import *
import math

#Convert euler harmony to music21 chord
def HertzToChord(h):
	pitches = []
	for t in h:
		p = math.trunc(round(12*math.log(t,2)))
		result = pitch.Pitch(p)
		#result.octave = 4 + p/12
		pitches.append(result)
	c = chord.Chord()
	#c.duration = duration.Duration('half')
	c.pitches = pitches
	c.addLyric(c.quality)
	return c

#works on euler harmonies
def inverse(h):
	result = []
	for t in h:
		result.append(1.0/t)
	return result

#works on euler harmonies
def product(h1, h2):
	result = []
	i = 0
	while i < len(h1) and i < len(h2):
		result.append(h1[i]*h2[i])
		i += 1
	return result

#works on euler harmonies
def translation(h, f):
	h2 = []
	for i in range(0,len(h)):
		h2.append(f)
	return product(h,h2)
