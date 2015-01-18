from operations import Duration, Parallel, Serial, Multiplication, Division, Frequency
from music21 import stream, note, interval
from math import log

unit_note = note.Note()
unit_note.pitch.frequency = 1
unit_note.duration.quarterLength = 1

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
        n.pitch.frequency = freq
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

    if isinstance(left, note.Note):
        result = transpose(right, left.pitch.frequency)
        result = scale_duration(result, left.quarterLength)
    elif isinstance(right, note.Note):
        result = transpose(left, right.pitch.frequency)
        result = scale_duration(result, right.quarterLength)
    else:
        raise NotImplementedError('Multiplication of two non-frequencies has no meaning')

    return result


def division(left, right):
    left = construct_music21(left)
    right = construct_music21(right)

    if isinstance(right, note.Note):
        result = transpose(left, 1 / right.pitch.frequency)
        result = scale_duration(result, 1 / right.quarterLength)
    else:
        raise NotImplementedError('Division by non-frequencies has no meaning')

    return result


def duration(left, right):
    subject = construct_music21(left)
    adject = construct_music21(right)
    scale = adject.pitch.frequency
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


def transpose(subject, freq):
    if isinstance(subject, note.Note):
        n = note.Note()
        n.duration = subject.duration
        n.pitch.frequency = subject.pitch.frequency * freq
        return n
    else:
        s = stream.Stream()
        for element in subject:
            s.insert(element.offset, transpose(element, freq))
            #s.append(transpose(element, freq))
        return s.flat


def scale_duration(subject, scale):
    if isinstance(subject, note.Note):
        return subject.augmentOrDiminish(scale, inPlace=False)
    else:
        subject = subject.scaleDurations(scale, inPlace=False)
        return subject.scaleOffsets(scale, inPlace=False)


def frequency_to_semitone(freq):
    return int(round(12 * log(freq, 2)))
