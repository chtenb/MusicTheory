import sys
from parseElr import parseElr

data = sys.stdin.read()
print(
    r'''
f1  0   4096    10 1 ; use GEN10 to compute a sine wave

;ins strt dur  amp(p4)   freq(p5)
''')

time = 0
tonic = 220.0
for chord in parseElr(data):
    duration = eval(chord[0][0])
    for pitch in chord[1]:
        print(r'i1  {time}  {duration}  4000   {pitch}'
                .format(time=time, duration=duration, pitch=eval(pitch)*tonic))
    time += duration

print(r'e ; indicates the end of the score')
