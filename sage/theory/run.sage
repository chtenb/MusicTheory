from harmony import Harmony
from composition import Composition
from composer import generate_melody, harmonize, tonal_space
import os

import metrics

# print '\n'.join([str(t) + ", " + str(metrics.harmonic_distance(t))
                 # for t in sorted(tonal_space())])
# exit()

name = "cmajor"

c = Composition.from_elr("./elr/" + name + ".elr")
for h in c.harmonies:
    print h.to_string(), h.position()
# c = harmonize(c)
# c = harmonize(c)

# c = generate_melody(20)
# c = harmonize(c)

# print c.to_string()
# m21 = c.to_music21_score_show_position(1, 1)
# m21.show()

# with open(name + ".elr", 'w') as f:
       # f.write(c.to_string())

# with open(name + ".sco", 'w') as f:
       # f.write(c.to_csound(440))

# os.system("csound orchestra.orc " + name + ".sco")
# os.system("gnome-open test.wav")
# print c.to_string()
