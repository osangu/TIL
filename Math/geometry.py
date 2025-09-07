from typing import Tuple, Union, List

from Math.base import Var


class Dot:

    def __init__(self, x: Var, y: Var):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x}, {self.y}'


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


class Shape:

    def __new__(cls, dots: List[Dot]) -> Union['Circle', 'Triangle', 'Square', 'Shape']:
        ...

class Circle(Shape):
    ...

class Triangle(Shape):

    def is_right(self) -> bool:
        ...

    def sin(self):
        if not self.is_right():
            raise
        ...

    def cos(self):
        if not self.is_right():
            raise
        ...

    def tan(self):
        if not self.is_right():
            raise

        ...


class Square(Shape):
    ...


if __name__ == '__main__':
    pythagorean_theorem(5, 12, 13)

    s: Circle = Shape(
        dots=[
            Dot(
                Var(name='x1'), Var(name='y1')
            ),
        ]
    )
    s2: Triangle = Shape(
        dots=[
            Dot(
                Var(name='x1'), Var(name='y1')
            ),
            Dot(
                Var(name='x2'), Var(name='y2')
            ),
            Dot(
                Var(name='x3'), Var(name='y3')
            ),
        ]
    )