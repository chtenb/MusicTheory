from composition import Composition
from harmony import Harmony
from metrics import (
    harmonic_distance, melodic_harmonic_distance, melodic_distance)


def tonal_space():
    """Return a set that we use as tonal space
    :returns: @todo

    """
    tonal_space = [2 ^ x * 3 ^ y * 5 ^ z for x in range(
        -4, 5) for y in range(-2, 3) for z in range(-2, 3)]
    # print sorted(tonal_space)
    return filter(lambda t: melodic_distance(t) < 12, tonal_space)


def generate_melody(length):
    """Generate a melody

    :length: number
    :returns: Composition

    """
    melody = Composition()
    melody.harmonies.append(Harmony([1], 1, 0))
    tones = tonal_space()
    for n in range(1, length - 1):
        tone = min(tones, key=lambda t: melody_tension(t, melody))
        print (str(tone) + " :  " + str(melody_tension(tone, melody)))
        h = Harmony([tone], 1, n)
        melody.harmonies.append(h)
    return melody


def melody_tension(t, melody):
    """Compute a value indicating the contextual tension of a tone

    :t: number
    :previous_tone: number
    :returns: number

    """
    if t in [h.tones[0] for h in melody.harmonies]:
        return 9999
    previous_tone = melody.harmonies[-1].tones[0]
    return N(harmonic_distance(1, t)
             + 2 * melodic_harmonic_distance(previous_tone, t))


def harmonize(c):
    """Attempt to add a voice to a composition

    :composition: Composition
    :returns: Composition

    """
    tones = tonal_space()

    previous_harmony = Harmony()
    previous_tone = 1
    for h in c.harmonies:
        new_tone = min(tones, key=lambda t: harmony_tension(t, h,
                       previous_tone, previous_harmony))
        print (str(new_tone) + " :  " + str(harmony_tension(new_tone, h,
               previous_tone, previous_harmony)))
        h.tones.append(new_tone)
        previous_harmony = h
        previous_tone = new_tone
    return c


def harmony_tension(t, h, prev_t, prev_h):
    """Compute a value indicating the contextual tension of a tone

    :t: tone
    :context: list of tones
    :returns: number

    """
    # Don't use tone if it's already used
    # Voices should keep melodical position
    if (t in h.tones
            # or t == prev_t
            or melodical_position(t, h) != melodical_position(prev_t, prev_h)):
        return 9999

    #return max(harmonic_distance(1, t),
               #sum([harmonic_distance(t, s) for s in h.tones])
               #/ len(h.tones)
               #)

    return N(harmonic_distance(1, t)
             + sum([harmonic_distance(t, s) for s in h.tones])
             / len(h.tones)
             )


def melodical_position(t, h):
    """Return an index indicating melodical position of t in h

    :t: number
    :h: harmony
    :returns: number

    """
    return len(filter(lambda s: s < t, h.tones))
