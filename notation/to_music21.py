from musicobject import Tone, Group, Transformed
from music21 import stream, note, duration
from math import log

#compound = stream.Stream()
#s1 = stream.Stream()
#s1.append(note.Note('C'))
#s1.append(note.Note('C'))
#s2 = stream.Stream()
#s2.append(note.Note('G'))
#s2.append(note.Note('F'))
#compound.insert(0, stream.Stream(stream.Stream(s1)))
#compound.insert(0, stream.Stream(stream.Stream(s2)))

#compound.semiFlat.show('text')
#compound.semiFlat.write('musicxml', 'bar.xml')


def construct_music21(musicobject):
    """Export a music21 stream from the given musicobject."""
    if type(musicobject) == Tone:
        if musicobject.frequency == '_':
            n = note.Rest()
        else:
            n = note.Note()
            n.pitch.name = musicobject.frequency
        n.duration.quarterLength = musicobject.duration
        return n

    if type(musicobject) == Group:
        compound = stream.Stream()
        for sequence in musicobject.sequences:
            s = stream.Stream()
            for element in sequence:
                s.append(construct_music21(element))
            compound.insert(0, s)
        return compound.flat

    if type(musicobject) == Transformed:
        subject = construct_music21(musicobject.subject)
        T = musicobject.transformation

        # Apply duration transformation
        subject.scaleDurations(T.duration)
        subject.scaleOffsets(T.duration)

        # Apply frequency transformation
        if isinstance(T.frequency, float):
            interval = frequency_to_semitone(T.frequency)
        else:
            interval = T.frequency
        subject.transpose(interval, inPlace=True)

        return subject


def frequency_to_semitone(frequency):
    return int(12 * log(frequency, 2))
