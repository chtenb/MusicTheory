import music21
from harmony import Harmony
import metrics
import re

Zarlino = [1 * 2 ^ -3, 3 ^ 2 / 2 ^ 3 * 2 ^ -3, 5 / 2 ^ 2 * 2 ^ -3, 2 ^ 2 / 3 * 2 ^ -3, 3 / 2 * 2 ^ -3, 5 / 3 * 2 ^ -3, (3 * 5) / 2 ^ 3 * 2 ^ -3] + [1 * 2 ^ -2, 3 ^ 2 / 2 ^ 3 * 2 ^ -2, 5 / 2 ^ 2 * 2 ^ -2, 2 ^ 2 / 3 * 2 ^ -2, 3 / 2 * 2 ^ -2, 5 / 3 * 2 ^ -2, (3 * 5) / 2 ^ 3 * 2 ^ -2] + [1 * 2 ^ -1, 3 ^ 2 / 2 ^ 3 * 2 ^ -1, 5 / 2 ^ 2 * 2 ^ -1, 2 ^ 2 / 3 * 2 ^ -1, 3 / 2 * 2 ^ -1, 5 / 3 * 2 ^ -1, (3 * 5) / 2 ^ 3 * 2 ^ -1] + [1 * 2 ^ 0, 3 ^ 2 / 2 ^ 3 * 2 ^ 0, 5 / 2 ^ 2 * 2 ^ 0, 2 ^ 2 / 3 * 2 ^ 0, 3 / 2 * 2 ^ 0, 5 / 3 * 2 ^ 0, (3 * 5) / 2 ^ 3 * 2 ^ 0] + [1 * 2 ^ 1, 3 ^ 2 / 2 ^ 3 * 2 ^ 1, 5 / 2 ^ 2 * 2 ^ 1, 2 ^ 2 / 3 * 2 ^ 1, 3 / 2 * 2 ^ 1, 5 / 3 * 2 ^ 1, (3 * 5) / 2 ^ 3 * 2 ^ 1] + [1 * 2 ^ 2, 3 ^ 2 / 2 ^ 3 * 2 ^ 2, 5 / 2 ^ 2 * 2 ^ 2, 2 ^ 2 / 3 * 2 ^ 2, 3 / 2 * 2 ^ 2, 5 / 3 * 2 ^ 2, (3 * 5) / 2 ^ 3 * 2 ^ 2] + [1 * 2 ^ 3, 3 ^ 2 / 2 ^ 3 * 2 ^ 3, 5 / 2 ^ 2 * 2 ^ 3, 2 ^ 2 / 3 * 2 ^ 3, 3 / 2 * 2 ^ 3, 5 / 3 * 2 ^ 3, (3 * 5) / 2 ^ 3 * 2 ^ 3]


class Composition:
    '''An timed set of harmonies'''
    harmonies = []

    @classmethod
    def from_music21_score(constructor, music21_score):
        '''Convert a music21 score to a Composition'''
        self = constructor()
        key = music21_score.analyze('key')
        tonic = key.getTonic()
        print 'Analysed tonic:', tonic
        if key.mode == 'minor':
            tonic = tonic.transpose(3)
            print 'Converted to:', tonic
        self.tonic = tonic.frequency
        for c in music21_score.flat.getElementsByClass(music21.chord.Chord):
            h = Harmony([], c.duration.quarterLength, c.offset)
            for p in c.pitches:
                tone_approximation = p.frequency / self.tonic
                tone = min(Zarlino, key=lambda z:
                           melodic_distance(tone_approximation, z))
                h.tones.append(tone)
            self.harmonies.append(h)
        return self

    @classmethod
    def from_elr(constructor, filename):
        """Convert a elr file to a Composition

        :filename: string
        :returns: Composition

        """
        self = constructor()
        with open(filename, 'r') as content_file:
            file = content_file.read()

            # The patterns we use
            pMatchHarmonies = re.compile(r'[(]([^|]+)[|]([^)]+)[)]')
            pMatchNumbers = re.compile(r'[\d/]+')

            sHarmonies = pMatchHarmonies.findall(file)
            end_of_last_harmony = 0
            for sHarmony in sHarmonies:
                sTiming = pMatchNumbers.findall(sHarmony[0])
                sTones = pMatchNumbers.findall(sHarmony[1])

                duration = sage_eval(sTiming[0])
                try:
                    offset = sage_eval(sTiming[1])
                except:
                    offset = end_of_last_harmony
                end_of_last_harmony = max(
                    end_of_last_harmony, offset + duration)

                tones = [sage_eval(t) for t in sTones]

                h = Harmony(tones, duration, offset)
                self.harmonies.append(h)

            return self

    def to_string(self):
        return ''.join([h.to_string() for h in self.harmonies])

    def to_csound(self, tonic, amplitude=4000):
        """Convert Composition to csound score

        :tonic: number
        :amplitude: number
        :returns: string

        """
        # Do shizzle hier
        result = "f1  0   4096    10 1  ; use GEN10 to compute a sine wave\n\n;ins strt dur amp(p4) freq(p5)\n"
        for h in self.harmonies:
            result += "\n" + h.to_csound(tonic, amplitude)
        result += "\n\ne"
        return result

    def to_music21_score(self, chords=None, tonic=440):
        '''Convert to a music21 score'''
        if chords is None:
            chords = [h.to_music21_chord() for h in self.harmonies]

        s = music21.stream.Stream()
        tonic_relative_to_c = tonic / music21.pitch.Pitch(0).frequency
        tonic_approximation_relative_to_c = round(
            log(tonic_relative_to_c) / log(pow(2, 1 / 12))
        )
        map(s.append, chords)
        s = s.transpose(tonic_approximation_relative_to_c)
        s.insert(0, s.bestClef())
        return s

    def to_music21_score_show_tones(self):
        '''Convert to a music21 score and show tones as lyrics'''
        return self.to_music21_score([h.to_music21_chord_show_tone() for h in self.harmonies])

    def to_music21_score_show_harmonic_distance(self):
        '''Convert to a music21 score and show subsequent harmonic_distance as lyrics'''
        chords = []
        chords.append(self.harmonies[0].to_music21_chord())
        for i in range(len(self.harmonies) - 1):
            chords.append(self.harmonies[i + 1].to_music21_chord_show_harmonic_distance(self.harmonies[i].tones[0]))
        return self.to_music21_score(chords)

    def to_music21_score_show_harmonic_distance_self(self):
        '''Convert to a music21 score and show harmonic_distance between first two tones as lyrics'''
        return self.to_music21_score([h.to_music21_chord_show_harmonic_distance_self() for h in self.harmonies])

    def to_music21_score_show_position(self, tonic=1, center=0):
        '''Convert to a music21 score and show position as lyrics'''
        return self.to_music21_score([h.to_music21_chord_show_position(tonic, center) for h in self.harmonies])

    def to_music21_score_show_melodic_distance(self):
        '''Convert to a music21 score and show subsequent melodic_distance as lyrics'''
        chords = []
        chords.append(self.harmonies[0].to_music21_chord())
        for i in range(len(self.harmonies) - 1):
            chords.append(self.harmonies[i + 1].to_music21_chord_show_melodic_distance(self.harmonies[i].tones[0]))
        return self.to_music21_score(chords)

    def to_music21_score_show_melodic_harmonic_distance(self):
        '''Convert to a music21 score and show subsequent melodic_distance as lyrics'''
        chords = []
        chords.append(self.harmonies[0].to_music21_chord())
        for i in range(len(self.harmonies) - 1):
            chords.append(self.harmonies[i + 1].to_music21_chord_show_melodic_harmonic_distance(self.harmonies[i].tones[0]))
        return self.to_music21_score(chords)

    def to_music21_score_show_melodic_harmonic_distance_self(self):
        '''Convert to a music21 score and show melodic_harmonic_distance between first two tones as lyrics'''
        return self.to_music21_score([h.to_music21_chord_show_melodic_harmonic_distance_self() for h in self.harmonies])

    def to_music21_score_show_melodic_and_harmonic_distance_self(self):
        return self.to_music21_score([h.to_music21_chord_show_melodic_and_harmonic_distance_self() for h in self.harmonies])

    def plot_melodic(self):
        ''' Plot the melodic norm for every first tone in the harmony'''
        sage.plot.plot.list_plot(
            [melodic_distance(h.tones[0], 1) for h in self.harmonies]).show()

    def plot_harmonic(self):
        ''' Plot the harmonic norm for every first tone in the harmony'''
        sage.plot.plot.list_plot(
            [harmonic_distance(h.tones[0], 1) for h in self.harmonies]).show()
