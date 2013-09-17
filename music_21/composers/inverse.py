from music21 import *
import math
import copy

def inverse(s,pitchName):
	#for p in s.getElementsByClass(stream.Part):
	#	for m in p.getElementsByClass(stream.Measure):
	#		for n in m.getElementsByClass(note.Note):
	b = pitch.Pitch(pitchName)
	result = copy.deepcopy(s)
	for n in result.flat.getElementsByClass(note.Note):
		newPitchClass = b.pitchClass-n.pitchClass
		#n.octave = n.octave + math.floor(newPitchClass/12)
		n.pitchClass = newPitchClass
	return result
