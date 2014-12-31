from musicobject import Tone, Group, Transformed
from music21 import stream, note, duration, interval
from math import log


def construct_music21(musicobject):
    """Export a music21 stream from the given musicobject."""
    if type(musicobject) == Tone:
        if isinstance(musicobject.frequency, float):
            n = note.Note()
            difference = frequency_to_semitone(musicobject.frequency)
            n.transpose(difference, inPlace=True)
        elif musicobject.frequency == '_':
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
            difference = frequency_to_semitone(T.frequency)
        else:
            difference = interval.notesToInterval(note.Note('c4'), note.Note(T.frequency))
        subject.transpose(difference, inPlace=True)

        return subject


def frequency_to_semitone(frequency):
    return int(round(12 * log(frequency, 2)))

