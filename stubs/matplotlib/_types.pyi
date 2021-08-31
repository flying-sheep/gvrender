from typing import Literal, Tuple, Union

_Color = Union[
    Tuple[float, float, float],
    Tuple[float, float, float, float],
    Literal['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'],
    Literal[
        'tab:blue',
        'tab:orange',
        'tab:green',
        'tab:red',
        'tab:purple',
        'tab:brown',
        'tab:pink',
        'tab:gray',
        'tab:olive',
        'tab:cyan',
    ],
    # #hex of lengths 3/6 (opaque) or 4/8 (alpha),
    # grey: '0.5',
    # a CSS4 color name: 'blue'
    # a XKCD color name: 'xkcd:sky blue'
    # a cycler index: 'C0'
    str,
]

_FontWeight = Literal[
    'ultralight',
    'light',
    'normal',
    'regular',
    'book',
    'medium',
    'roman',
    'semibold',
    'demibold',
    'demi',
    'bold',
    'heavy',
    'extra bold',
    'black',
]

_FontStretch = Literal[
    'ultra-condensed',
    'extra-condensed',
    'condensed',
    'semi-condensed',
    'normal',
    'semi-expanded',
    'expanded',
    'extra-expanded',
    'ultra-expanded',
]

_FontSize = Literal['xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
