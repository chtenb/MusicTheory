from pyparsing import Regex, OneOrMore, Forward


fraction = Regex(r'\d+(/\d+)?')

frequency_symbol = Regex(r'[abcdefg_]\d?[#b]?')
frequency_number = fraction
frequency = frequency_number ^ frequency_symbol
duration = fraction

transformation = '(' + frequency + ',' + duration + ')'

music_object = Forward()
group = '{' + OneOrMore(music_object) + '}'
music_object << (frequency ^ group ^ (transformation + group))


example = """
{
    (c4, 5) {c c# g g a a g _ f f e e db b b d c}
}
"""
result = music_object.parseString(example)
print(result)
