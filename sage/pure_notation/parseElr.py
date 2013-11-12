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
