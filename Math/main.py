from typing import Union, List

basic_operation = {
    '+': lambda x, y: (x + y),
    '-': lambda x, y: (x - y),
    '*': lambda x, y: (x * y),
    '/': lambda x, y: (x / y),
}



class Formula:

    def __init__(self, args: List['Var']):
        self.variables = args

    def __repr__(self):
        return ' '.join(
            [
                str(v)
                for v in self.variables
            ]
        )

    def __add__(self, other: Union[int, 'Var', 'Formula']):
        return Formula([*self.variables, '+', other])

    def __sub__(self, other):
        return Formula([*self.variables, '-', other])

    def __mul__(self, other):
        return Formula([*self.variables, '*', other])

    def __truediv__(self, other):
        return Formula([*self.variables, '/', other])


class Var:

    def __init__(self, name: str, time: int = 1, exponent: int = 1):
        self._name = name
        self._time = time
        self._exponent = exponent

    def __repr__(self):
        t, e = '', ''

        if self._time != 1:
            t = f'{self._time} * '

        if self._exponent != 1:
            e = f'^{self._exponent}'

        return f'{t}{self._name}{e}'

    def value(self, v: int):
        return self._time * (v ** self._exponent)

    def __add__(self, other: Union[int, 'Var']):
        return Formula([self, '+', other])

    def __sub__(self, other):
        return Formula([self, '-', other])

    def __mul__(self, other):
        return Formula([self, '*', other])

    def __truediv__(self, other):
        return Formula([self, '/', other])

    '''
    def __floordiv__(self, other):  # //
        ...

    def __mod__(self, other):  # %
        ...

    def __pow__(self, other):  # **
        ...
    '''


def pythagorean_theorem(a_v, b_v, c_v):
    a = Var(name='a', exponent=2)
    b = Var(name='b', exponent=2)
    c = Var(name='c', exponent=2)

    print(
        f'{str(c)} = {str(a)} + {str(b)}'
    )
    print(
        f'{c.value(c_v)} = {a.value(a_v)} + {b.value(b_v)}'
    )

if __name__ == '__main__':
    pythagorean_theorem(5, 12, 13)

    '''    
    class Args:
    
        def __init__(self, *args):
            if len(args) > Args.length:
                raise IndexError(f'Args length should be under {Args.length}')
    
            self.args = tuple(args)
    
        def __class_getitem__(cls, _: int):
            cls.length = _
    
            return cls
    
    '''
