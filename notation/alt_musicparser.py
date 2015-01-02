from pyparsing import (Regex, OneOrMore, Forward, delimitedList, restOfLine, Group as Grp,
                       Suppress, Optional, operatorPrecedence, opAssoc, ParseException, oneOf,
                       ParserElement)
from alt_musicobject import Tone, Group, Transformed
ParserElement.enablePackrat()


comment = '#' + restOfLine

number = Regex(r'\d*[.]?\d+')
number.setParseAction(lambda s, l, t: [float(t[0])])
frequency_symbol = Regex(r'[abcdefg_]\d?[#-]?')
frequency = number ^ frequency_symbol

musicobject = operatorPrecedence(frequency, [
    (oneOf('/ *'), 2, opAssoc.LEFT),
    ('|', 2, opAssoc.LEFT),
    (Optional('>', default='>'), 2, opAssoc.LEFT),
    (',', 2, opAssoc.LEFT)
])
musicobject.ignore(comment)


result = musicobject.parseFile('alt_example.music')
print(result)

#from to_music21 import construct_music21
#construct_music21(result[0]).write('musicxml', 'foo.xml')
# construct_music21(result[0]).show('text')
