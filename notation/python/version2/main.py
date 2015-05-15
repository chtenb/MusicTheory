from maparser import parse_file
from subprocess import call
call(["ls", "-l"])

test = parse_file('example.ma')
print(test)
from to_music21 import construct_music21
m21_result = construct_music21(test)
m21_result.show('text')
#m21_result.show('midi')
#m21_result.show('vexflow')
#m21_result.show('lily.png')
#m21_result.show('musicxml')
#m21_result.show('lily')
#m21_result.show('musicxml.png')
m21_result.write('midi', 'output/foo.mid')
call(['midi2ly', 'output/foo.mid', '-o', 'output/foo.ly'])
call(['lilypond', '-o', 'output/foo', 'output/foo.ly'])

#m21_result.write('lily.png', 'output/foo')
