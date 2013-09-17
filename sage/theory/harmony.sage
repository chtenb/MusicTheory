import music21


class Harmony:
    '''Class representing a pure chord'''
    def __init__(self, tones=[], duration=1, offset=0):
        self.tones = tones
        self.duration = duration
        self.offset = offset

    def position(self, tonic=1, center=0):
        result = 0
        weights = {2: 0, 3: 2, 5: 3}
        for t in self.tones:
            for p in list(factor(t / tonic)):
                result += weights[p[0]] * p[1]
        return result - center

    def to_string(self):
        result = '(' + str(self.duration)
        if bool(self.offset):
            result += ' ' + str(self.offset)
        result += '|'
        result += ','.join([str(t) for t in self.tones])
        result += ') '
        return result

    def to_csound(self, tonic, amplitude):
        """Convert harmony to csound score line"""
        result = ""
        for tone in self.tones:
            result += "\ni1 %d %d %d %d" % (
                self.offset, self.duration, amplitude, tonic * tone)
        return result

    def to_12_tone_scale(self):
        '''Compute the closest tone in the 12 tone equal scale,
        for each tone in self'''
        return [round(log(t) / log(pow(2, 1 / 12))) for t in self.tones]

    def to_music21_chord(self):
        '''Convert to a music21 chords'''
        approximation = self.to_12_tone_scale()
        pitches = [music21.pitch.Pitch(pitchClass=t % 12, octave=int(
            t / 12) + 4) for t in approximation]
        chord = music21.chord.Chord(pitches)
        chord.duration = music21.duration.Duration(self.duration)
        chord.offset = self.offset
        return chord

    def to_music21_chord_show_tone(self):
        '''Convert to a music21 chords and show tone as lyric'''
        chord = self.to_music21_chord()
        text = '\n'.join([str(t) for t in sorted(self.tones, reverse=True)])
        chord.addLyric(text)
        return chord

    def to_music21_chord_show_harmonic_distance_to_tonic(self, tone):
        '''Convert to a music21 chords and show harmonic_distance
        between first tone and given tone as lyric'''
        chord = self.to_music21_chord()
        chord.addLyric(str(harmonic_distance(self.tones[0], tone)) +
                       '\n' + str(harmonic_distance(self.tones[0], 1)))
        # chord.addLyric((harmonic_distance(self.tones[0],
        # tone))+(harmonic_distance(self.tones[0], 1)))
        return chord

    def to_music21_chord_show_harmonic_distance_self(self):
        '''Convert to a music21 chords and show harmonic_distance
        between first two tone in self as lyric'''
        chord = self.to_music21_chord()
        chord.addLyric(harmonic_distance(self.tones[0], self.tones[1]))
        return chord

    def to_music21_chord_show_position(self, tonic=1, center=0):
        '''Convert to a music21 chords and show position
        between first tone and given tone as lyric'''
        chord = self.to_music21_chord()
        # Apparently midi cannot display negative numbers in lyrics :(
        chord.addLyric(str(self.position(tonic, center)))
        return chord

    def to_music21_chord_show_harmonic_distance(self, tone):
        '''Convert to a music21 chords and show harmonic_distance
        between first tone and given tone as lyric'''
        chord = self.to_music21_chord()
        # chord.addLyric((harmonic_distance(self.tones[0],
        # tone))+(harmonic_distance(self.tones[0], 1)))
        chord.addLyric(harmonic_distance(self.tones[0], tone))
        return chord

    def to_music21_chord_show_melodic_distance_self(self):
        '''Convert to a music21 chords and show melodic_distance
        between first two tone in self as lyric'''
        chord = self.to_music21_chord()
        chord.addLyric(melodic_distance(self.tones[0], self.tones[1]))
        return chord

    def to_music21_chord_show_melodic_distance(self, tone):
        '''Convert to a music21 chords and show melodic_distance
        between first tone and given tone as lyric'''
        chord = self.to_music21_chord()
        chord.addLyric(round(N(melodic_distance(self.tones[0], tone))))
        return chord

    def to_music21_chord_show_melodic_harmonic_distance(self, tone):
        '''Convert to a music21 chords and show melodic_distance
        between first tone and given tone as lyric'''
        chord = self.to_music21_chord()
        chord.addLyric(round(N(melodic_distance(
            self.tones[0], tone))) + harmonic_distance(self.tones[0], tone))
        return chord

    def to_music21_chord_show_melodic_harmonic_distance_self(self):
        '''Convert to a music21 chords and show melodic_distance
        between first tone and given tone as lyric'''
        chord = self.to_music21_chord()
        chord.addLyric(round(N(melodic_distance(self.tones[0], self.tones[1])))
                       + harmonic_distance(self.tones[0], self.tones[1]))
        return chord

    def to_music21_chord_show_melodic_and_harmonic_distance_self(self):
        chord = self.to_music21_chord()
        chord.addLyric(
            str(harmonic_distance(self.tones[0], self.tones[1]))
            + '\n'
            + str(round(n(melodic_distance(self.tones[0], self.tones[1]))))
        )
        # chord.addLyric((harmonic_distance(self.tones[0],
        # tone))+(harmonic_distance(self.tones[0], 1)))
        return chord
