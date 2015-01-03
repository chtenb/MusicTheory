import pyparsing as pp
from operations import Parallel, Serial, Duration, Division, Multiplication, Frequency
pp.ParserElement.enablePackrat()


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

number = pp.Regex(r'\d*[.]?\d+')
#number.setParseAction(lambda s, l, t: [num(t[0])])

frequency_symbol = pp.Regex(r'[abcdefg_]\d?[#-]?')
frequency = number ^ frequency_symbol


def frequency_action(s, l, t):
    t = t.asList()[0]
    return [Frequency(t)]
frequency.setParseAction(frequency_action)
#frequency.setParseAction(lambda s, l, t: [num(t[0])])


mul = pp.oneOf('/ *')


def mul_action(s, l, t):
    tokens = t.asList()[0]
    result = tokens[0]
    i = 1
    while i < len(tokens) - 1:
        if tokens[i] == '*':
            result = Multiplication(result, tokens[i + 1])
        elif tokens[i] == '/':
            result = Division(result, tokens[i + 1])
        else:
            raise ValueError('Bogus multiplicative expression.')

        i += 2

    return result


duration = pp.Literal('|')


def duration_action(s, l, t):
    tokens = [t for t in t.asList()[0] if t != '|']
    result = tokens[0]
    for token in tokens[1:]:
        result = Duration(result, token)
    return result


serial = pp.Optional(pp.Empty(), default='')


def serial_action(s, l, t):
    tokens = t.asList()[0]
    result = tokens[0]
    for token in tokens[1:]:
        result = Serial(result, token)
    return result


parallel = pp.Literal(',')


def parallel_action(s, l, t):
    tokens = [t for t in t.asList()[0] if t != ',']
    result = tokens[0]
    for token in tokens[1:]:
        result = Parallel(result, token)
    return result


maobject = pp.operatorPrecedence(frequency, [
    (mul, 2, pp.opAssoc.LEFT, mul_action),
    (duration, 2, pp.opAssoc.LEFT, duration_action),
    (serial, 2, pp.opAssoc.LEFT, serial_action),
    (parallel, 2, pp.opAssoc.LEFT, parallel_action)
])

comment = '#' + pp.restOfLine
maobject.ignore(comment)


def parse_file(filename):
    return maobject.parseFile(filename)

print(parse_file('example.ma'))

#from to_music21 import construct_music21
#construct_music21(result[0]).write('musicxml', 'foo.xml')
# construct_music21(result[0]).show('text')
