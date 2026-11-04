import math
import sys
import os
print(sys.path)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ast_nodes as a

new_vars = {
    "sin": lambda x: a.Number(math.sin(x)),
    "cos": lambda x: a.Number(math.cos(x)),
    "tan": lambda x: a.Number(math.tan(x)),

    "asin": lambda x: a.Number(math.asin(x)),
    "acos": lambda x: a.Number(math.acos(x)),
    "atan": lambda x: a.Number(math.atan(x)),

    "atan2": lambda y, x: a.Number(math.atan2(y, x)),

    "sinh": lambda x: a.Number(math.sinh(x)),
    "cosh": lambda x: a.Number(math.cosh(x)),
    "tanh": lambda x: a.Number(math.tanh(x)),

    "asinh": lambda x: a.Number(math.asinh(x)),
    "acosh": lambda x: a.Number(math.acosh(x)),
    "atanh": lambda x: a.Number(math.atanh(x)),

    "hypot": lambda *args: a.Number(math.hypot(*args)),

    "log": lambda x: a.Number(math.log(x)),
    "exp": lambda x: a.Number(math.exp(x)),

    "sqrt": lambda x: a.Number(math.sqrt(x)),
    "root": lambda x, y: a.Number(x ** (1 / y)),

    "radians": lambda x: a.Number(math.radians(x)),
    "degrees": lambda x: a.Number(math.degrees(x)),

    "pi": a.Number(3.141592653589793),
    "tau": a.Number(6.283185307179586),
    "e": a.Number(2.718281828459045),
    "phi": a.Number(1.618033988749894)
    }
