from pyparsing import Regex, OneOrMore, Forward, delimitedList, restOfLine, Group as Grp, Dict, Suppress
from musicobject import Tone, Group, Transformed


music_object = Forward()

comment = '#' + restOfLine
music_object.ignore(comment)

fraction = Regex(r'\d+(/\d+)?')
fraction.setParseAction(lambda s, l, t: [float(t[0])])

frequency_symbol = Regex(r'[abcdefg_]\d?[#b]?')
frequency_number = fraction
frequency = frequency_number ^ frequency_symbol

duration = fraction

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
    (2, 1) * {c c g g a a g _ f f e e d d c},
    (1, 2) * {c   e   f   e   d   c   g   c}
}
"""
    #{c   e   f   e,   d   c   g   (c, 1)},
    #(c4, 5) * {c c# g g a a g _ f f e e db b b d c} #asf
    #(c4, 5) * {c c# g g a a g _ f f e e db b b d c}, #asf
    #(c3, 2) * {c   e   f   e   d   c   g   (c, 1)}
result = music_object.parseString(example)
print(result[0])

from to_music21 import construct_music21
construct_music21(result[0]).write('musicxml', 'foo.xml')
construct_music21(result[0]).show('text')
