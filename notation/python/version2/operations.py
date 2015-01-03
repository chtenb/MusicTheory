"""
This module contains building blocks for music arithmetic expressions.
"""


class Frequency:

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return str(self.token)


class BinaryOperation:

    formatstring = 'BinaryOperation({}, {})'

    def __init__(self, operand1, operand2):
        self.operands = (operand1, operand2)

    def __getitem__(self, index):
        return self.operands[index]

    def __repr__(self):
        return self.formatstring.format(*self.operands)


class Multiplication(BinaryOperation):

    formatstring = '{} * {}'


class Division(BinaryOperation):
    formatstring = '{} / {}'


class Duration(BinaryOperation):
    formatstring = '({} | {})'


class Serial(BinaryOperation):
    formatstring = '({} {})'


class Parallel(BinaryOperation):
    formatstring = '({}, {})'
