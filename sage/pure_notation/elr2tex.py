import sys
from parseElr import parseElr

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
