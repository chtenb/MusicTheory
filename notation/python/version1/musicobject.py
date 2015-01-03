
class Tone:

    def __init__(self, frequency, duration=1):
        self.frequency = frequency
        self.duration = duration

    def __repr__(self):
        return (str(self.frequency) if self.duration == 1
                else '({}, {})'.format(self.frequency, self.duration))


class Group:

    def __init__(self, sequences):
        self.sequences = sequences

    def __repr__(self):
        return '{{{}}}'.format(', '.join(' '.join(str(t) for t in s) for s in self.sequences))


class Transformed:

    def __init__(self, transformation, subject):
        self.transformation = transformation
        self.subject = subject

    def __repr__(self):
        return str(self.transformation) + ' * ' + str(self.subject)

