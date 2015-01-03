from operations import Duration, Parallel, Serial, Multiplication, Frequency
from music21 import stream, note, interval
from math import log


def construct_music21(musicobject):
    """Export a music21 stream from the given musicobject."""
    if type(musicobject) == Frequency:
        try:
            frequency = float(musicobject.token)
            n = note.Note()
            semitones = frequency_to_semitone(frequency)
            n.transpose(semitones, inPlace=True)
        except ValueError:
            if musicobject.frequency == '_':
                n = note.Rest()
            else:
                n = note.Note()
                n.pitch.name = musicobject.token
            n.duration.quarterLength = musicobject.duration
        return n

    if type(musicobject) == Parallel:
        compound = stream.Stream()
        for element in musicobject.elements:
            s = stream.Stream()
            compound.insert(0, element)
        return compound.flat

    if type(musicobject) == Serial:
        s = stream.Stream()
        for element in musicobject.elements:
            s.append(construct_music21(element))
        return s

    if type(musicobject) == Duration:
        subject = construct_music21(musicobject.elements[0])
        return scale_duration(subject, musicobject)

    if type(musicobject) == Multiplication:
        tokens = musicobject.tokens
        i = 1
        folded = construct_music21(tokens[0])
        while i < len(tokens) - 1:
            if tokens[i] == '*':
                folded = multiply(folded, tokens[i + 1])
            elif tokens[i] == '/':
                ...
            else:
                raise ValueError('Bogus multiplication operands.')

        return folded


def multiply(subject, operand):
    if type(operand) == Frequency:
        return transpose(subject, operand)
    if type(operand) == Duration:
        return scale_duration(subject, operand)


def transpose(subject, frequency):
    try:
        frequency = float(frequency.token)
        difference = frequency_to_semitone(frequency)
    except ValueError:
        difference = interval.notesToInterval(note.Note('c1'), note.Note(frequency))

    return subject.transpose(difference)


def scale_duration(subject, duration):
    factor = 1
    for element in duration.elements[1:]:
        factor *= float(element)

    if isinstance(subject, note.Note):
        return subject.augmentOrDiminish(factor, inPlace=False)
    else:
        subject = subject.scaleDurations(factor, inPlace=False)
        return subject.scaleOffsets(factor, inPlace=False)


def frequency_to_semitone(frequency):
    return int(round(12 * log(frequency, 2)))
