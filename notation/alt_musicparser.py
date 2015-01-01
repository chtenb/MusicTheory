from pyparsing import (Regex, OneOrMore, Forward, delimitedList, restOfLine, Group as Grp,
                       Suppress, Optional, operatorPrecedence, opAssoc, ParseException)
from alt_musicobject import Tone, Group, Transformed


comment = '#' + restOfLine

number = Regex(r'\d*[.]?\d+')
number.setParseAction(lambda s, l, t: [float(t[0])])

scalar = operatorPrecedence(number, [
    ('/', 2, opAssoc.LEFT),
    ('*', 2, opAssoc.LEFT),
])
#number.setParseAction(lambda s, l, t: [eval(t[0])])

#result = scalar.parseString('3/(4*7)')
#print(result[0])
#exit()

frequency_symbol = Regex(r'[abcdefg_]\d?[#-]?')
frequency = scalar ^ frequency_symbol
duration = scalar

tone = frequency + Optional('|' + duration)
#tone.setParseAction(lambda s, l, t: Tone(*t))

musicobject = Forward()

series = OneOrMore(musicobject)
parallel = delimitedList(Grp(series), ',')

group = (('(' + series + ')') ^ ('(' + parallel + ')')) + Optional('|' + duration)
#group = ('(' + OneOrMore(musicobject) + ')')
#group.setParseAction(lambda s, l, t: Group(t))

transformed = operatorPrecedence(tone ^ group, [
    ('/', 2, opAssoc.LEFT),
    ('*', 2, opAssoc.LEFT),
])
#transformed = (tone + '*' + musicobject) ^ (musicobject + '/' + tone)
#transformed.setParseAction(lambda s, l, t: Transformed(t[0], t[2]))

#musicobject << (tone ^ group)
musicobject << (tone ^ group ^ transformed)
musicobject.ignore(comment)


#try:
    #musicobject.validate()
#except ParseException as err:
    #print(err.line)
    #print(" "*(err.column-1) + "^")
    #print(err)
result = musicobject.parseFile('alt_example.music')
print(result)

#from to_music21 import construct_music21
#construct_music21(result[0]).write('musicxml', 'foo.xml')
# construct_music21(result[0]).show('text')
