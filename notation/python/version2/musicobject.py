
class Frequency:

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return str(self.token)

class Multiplication:

    def __init__(self, tokens):
        self.tokens = tokens

    def __repr__(self):
        return ''.join([str(t) for t in self.tokens])

class Duration:

    def __init__(self, elements):
        #if len(elementl) != 2:
            #raise ValueError('Duration should only have 2 arguments')
        #self.subject = elements[0]
        #self.value = elements[1]
        self.elements = elements

    def __repr__(self):
        return '({})'.format(' | '.join(str(e) for e in self.elements))

class Serial:

    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return '({})'.format(' '.join(str(e) for e in self.elements))

class Parallel:

    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return '({})'.format(', '.join(str(e) for e in self.elements))

