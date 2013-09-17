# Read midi file using music21 and convert to pure file
import music21
from composition import composition

#sBach = music21.corpus.parse('bach/bwv7.7')
sPachelbel = music21.converter.parse('/home/chiel/Desktop/Pachelbel - Canon in D.mxl')
#sPachelbel.show()
#exit()

part1 = sPachelbel.getElementsByClass(music21.stream.Part)[0].getElementsByClass(music21.stream.Measure)[12:17]
part2 = sPachelbel.getElementsByClass(music21.stream.Part)[1].getElementsByClass(music21.stream.Measure)[12:17]

#Now merge the two parts into one stream, such that we can analyze metrics easily
merged = music21.stream.Stream()
for n in part1.flat.getElementsByClass(music21.note.Note):
    try:
        m = part2.flat.getElementsByClass(music21.note.Note).getElementsByOffset(n.offset)[0]
        c = music21.chord.Chord([n,m])
    except:
        c = music21.chord.Chord([n])
    merged.append(c)
#print list(merged.flat.getElementsByClass(music21.chord.Chord))
#merged.show()
piece = composition.from_music21_score(merged)
piece.to_music21_score_show_melodic_and_harmonic_distance_self().show()
#piece.to_music21_score_show_tones().show()

#piece.to_music21_score_show_harmonic_distance().show()
#piece.to_music21_score_show_melodic_distance().show()
#piece.to_music21_score_show_melodic_harmonic_distance().show()
#piece.to_music21_score().show()
