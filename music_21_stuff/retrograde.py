from music21 import *
import math

print "Parsing file..."
s = corpus.parse('bach/bwv1.6.mxl')

print "Transforming data"
#for n in s.flat.getElementsByClass(note.Note):
#	n.offset = s.flat.highestOffset - n.offset
#	n.addLyric(n.offset)
#s.sort()

print "Sending to MuseScore..."
s.show('musicxml')
