# Numbers can be constructed by the usual expressions.
# Numbers are frequencies by default.
# A duration parameter can be specified after a `|` symbol, which has a low precedence
# Parenthesis are not needed for tuples anymore, so they can replace curly brackets.
#
# So we have the rationals with the usual operators
# `*` and `/` (precedence 4)
# extended with frequency constants and the operators
# `|` (duration operator, precedence 3)
# ` ` (serial operator, precedence 2)
# `,` (parallel operator, precedence 1)

# The advantage of choosing this precedence order is that we can write multiple voices easily
c g a g f e (d d) | 2 c,
c e f e d c g |4          c
# The disadvantage of choosing this precedence order is that writing chords requires parenthesis
#(
    #c (e, g) (f, a) (e, g) (f, a) (e, g) (g/2, (d d) | 1/2) c
#)

# If we swap the precedence order of `,` and ` `, the parts would look like this
#(
    #(c g a g f e (d d) | 1/2 c),
    #(c e f e d c g           c)
#)
#(
    #c e, g f, a e, g f, a e, g g/2, (d d) | 1/2 c
#)
# Although it requires less parenthesis, it is also less readable,
# because intuitively commas are seperators, more than spaces

# If we swap the meaning of `,` and ` `, the parts would look like this
#(
    #(c, g, a, g, f, e, (d, d) | 1/2, c),
    #(c, e, f, e, d, c, g,            c)
#)
#(
    #c, e g, f a, e g, f a, e g, g/2 (d, d) | 1/2, c
#)

# In practice you would place parenthesis around chords and melodies anyway, to specify duration
# So it doesn't matter much
