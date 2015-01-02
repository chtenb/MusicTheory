import pyparsing as pp
from alt_musicobject import Parallel, Serial, Duration
pp.ParserElement.enablePackrat()


comment = '#' + pp.restOfLine

number = pp.Regex(r'\d*[.]?\d+')
number.setParseAction(lambda s, l, t: [float(t[0])])
frequency_symbol = pp.Regex(r'[abcdefg_]\d?[#-]?')
frequency = number ^ frequency_symbol

mul = pp.oneOf('/ *')
duration = pp.Literal('|')
def duration_action(s, l, t):
    t = t.asList()[0]
    return [Duration([x for x in t if x != '|'])]

serial = pp.Optional(pp.Empty(), default='')
def serial_action(s, l, t):
    t = t.asList()[0]
    return [Serial(t)]

parallel = pp.Literal(',')
def parallel_action(s, l, t):
    t = t.asList()[0]
    return [Parallel([x for x in t if x != ','])]

musicobject = pp.operatorPrecedence(frequency, [
    (mul, 2, pp.opAssoc.LEFT),
    (duration, 2, pp.opAssoc.LEFT, duration_action),
    (serial, 2, pp.opAssoc.LEFT, serial_action),
    (parallel, 2, pp.opAssoc.LEFT, parallel_action)
])
musicobject.ignore(comment)


result = musicobject.parseFile('alt_example.music')
print(result[0])

#from to_music21 import construct_music21
#construct_music21(result[0]).write('musicxml', 'foo.xml')
# construct_music21(result[0]).show('text')
