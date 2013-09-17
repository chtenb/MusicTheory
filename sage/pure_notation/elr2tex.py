import sys
import re


def parseElr(s):
    pSplitOnSpace = re.compile(r'\s')
    #The chords in string format
    sChords = pSplitOnSpace.split(s)

    pMatchChordParts = re.compile(r'[(][\d,/]+[)]')
    lChords = []
    for sChord in sChords:
        #The parts of a chord (pitch and time) in string format
        sChordParts = pMatchChordParts.findall(sChord)
        if bool(sChordParts):
            lChord = []
            for sChordPart in sChordParts:
                pMatchNumbers = re.compile(r'[\d/]+')
                #The rational numbers contained in the chordParts
                #in string format
                sNumbers = pMatchNumbers.findall(sChordPart)
                lChord.append(sNumbers)
            lChords.append(lChord)
    return lChords

data = sys.stdin.read()
print r'\setlength{\unitlength}{10pt}'
for chord in parseElr(data):
    print r'\begin{picture}(2,5)'

    #Print pitches
    i = 0
    for pitch in chord[1]:
        print r'\put(0,' + str(i) + r'){\makebox(0, 0){$' + str(pitch) + r'$}}'
        i += 1
    print r'\put(0,' + str(i) + r'){\oval(3,2)}'

    #Print timings
    print r'\put(-0.5,' + str(i) + r'){\makebox(0, 0){$' + str(chord[0]
                                                               [0]) + r'$}}'
    print r'\put(0.5,' + str(i) + r'){\makebox(0, 0){$' + str(chord[0][
                                                              1]) + r'$}}'
    print r'\put(0,1){\oval(2,4)}'

    print r'\end{picture}'
