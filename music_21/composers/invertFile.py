from music21 import *
import math
import inverse
import sys

filename = sys.argv[1]
axis = sys.argv[2]

print "Parsing file..."
#s = corpus.parse(filename)
s = converter.parse(filename)
print "File parsed"
newS = inverse.inverse(s,axis)
print "Sending to MuseScore..."
newS.show('midi')
