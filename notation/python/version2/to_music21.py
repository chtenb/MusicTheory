from operations import Duration, Parallel, Serial, Multiplication, Division, Frequency
from music21 import stream, note, interval
from math import log


def construct_music21(maobject):
    """Export a music21 stream from the given maobject."""
    if type(maobject) == Frequency:
        return frequency(maobject.token)

    if type(maobject) == Multiplication:
        return multiplication(*maobject)

    if type(maobject) == Division:
        return division(*maobject)

    if type(maobject) == Duration:
        return duration(*maobject)

    if type(maobject) == Serial:
        return serial(*maobject)

    if type(maobject) == Parallel:
        return parallel(*maobject)

    raise ValueError('Given object not a music arithmatic object.')


def frequency(freq):
    try:
        freq = float(freq)
        n = note.Note()
        semitones = frequency_to_semitone(freq)
        n.transpose(semitones, inPlace=True)
    except ValueError:
        if freq == '_':
            n = note.Rest()
        else:
            n = note.Note()
            n.pitch.name = freq
    return n


def multiplication(left, right):
    left = construct_music21(left)
    right = construct_music21(right)

    if isinstance(left, note.Note) and isinstance(right, note.Note):
        result = note.Note()

    raise NotImplementedError


def division(left, right):
    raise NotImplementedError


def duration(left, right):
    subject = construct_music21(left)
    scale = float(right.token) # Only numbers are allowed as duration
    return scale_duration(subject, scale)


def serial(left, right):
    s = stream.Stream()
    for element in (left, right):
        s.append(construct_music21(element))
    return s.flat


def parallel(left, right):
    s = stream.Stream()
    for element in (left, right):
        s.insert(0, construct_music21(element))
    return s.flat


#
# Helper functions
#


def transpose(subject, frequency):
    try:
        frequency = float(frequency.token)
        difference = frequency_to_semitone(frequency)
    except ValueError:
        difference = interval.notesToInterval(note.Note('c1'), note.Note(frequency))

    return subject.transpose(difference)


def scale_duration(subject, scale):
    if isinstance(subject, note.Note):
        return subject.augmentOrDiminish(scale, inPlace=False)
    else:
        subject = subject.scaleDurations(scale, inPlace=False)
        return subject.scaleOffsets(scale, inPlace=False)


def frequency_to_semitone(frequency):
    return int(round(12 * log(frequency, 2)))
