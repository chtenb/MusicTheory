from pyparsing import Regex, OneOrMore, Forward, delimitedList, restOfLine, Group as Grp, Dict, Suppress
from musicobject import Tone, Group, Transformed


music_object = Forward()

comment = '#' + restOfLine
music_object.ignore(comment)

#fraction = Regex(r'(\d*[./]?\d*)')
number = Regex(r'[\d./]+')
number.setParseAction(lambda s, l, t: [float(eval(t[0]))])

frequency_symbol = Regex(r'[abcdefg_]\d?[#-]?')
frequency_number = number
frequency = frequency_number ^ frequency_symbol

duration = number

tone = frequency ^ (Suppress('(') + frequency + Suppress(',') + duration + Suppress(')'))
tone.setParseAction(lambda s, l, t: Tone(*t))

group = Suppress('{') + delimitedList(Grp(OneOrMore(music_object)), ',') + Suppress('}')
group.setParseAction(lambda s, l, t: Group(t))

transformed = tone + '*' + group
transformed.setParseAction(lambda s, l, t: Transformed(t[0], t[2]))
music_object << (tone ^ group ^ transformed)


example = """
{
    # This is a comment
    (c5, 1) * {c c g g a a g _ (1, 1/2) * {f _} f e e d d (c, 2)},
    (1, 2) * {c   e   f   e   d                   c   g   c}
}
"""
    #(2, 1) * {c c g g a a g _ (f, 1/2) (_, 1/2) f e e d d (c, 2)},

result = music_object.parseString(example)
print(result[0])

from to_music21 import construct_music21
construct_music21(result[0]).write('musicxml', 'foo.xml')
construct_music21(result[0]).show('text')
