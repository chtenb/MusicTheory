from pyparsing import (Regex, OneOrMore, Forward, delimitedList, restOfLine, Group as Grp,
                       Suppress)
from musicobject import Tone, Group, Transformed


musicobject = Forward()

comment = '#' + restOfLine
musicobject.ignore(comment)

#fraction = Regex(r'(\d*[./]?\d*)')
number = Regex(r'[\d./]+')
number.setParseAction(lambda s, l, t: [float(eval(t[0]))])

frequency_symbol = Regex(r'[abcdefg_]\d?[#-]?')
frequency_number = number
frequency = frequency_number ^ frequency_symbol

duration = number

tone = frequency ^ (Suppress('(') + frequency + Suppress(',') + duration + Suppress(')'))
tone.setParseAction(lambda s, l, t: Tone(*t))

group = Suppress('{') + delimitedList(Grp(OneOrMore(musicobject)), ',') + Suppress('}')
group.setParseAction(lambda s, l, t: Group(t))

transformed = tone + '*' + musicobject
transformed.setParseAction(lambda s, l, t: Transformed(t[0], t[2]))
musicobject << (tone ^ group ^ transformed)


result = musicobject.parseFile('example.music')
print(result[0])

from to_music21 import construct_music21
construct_music21(result[0]).write('musicxml', 'foo.xml')
construct_music21(result[0]).show('text')
