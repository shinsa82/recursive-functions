import logging
from logging import basicConfig, getLogger, DEBUG
from termcolor import colored

print(logging.BASIC_FORMAT)

basicConfig(level=DEBUG, format=colored(logging.BASIC_FORMAT, 'cyan'))
logger = getLogger('primrec')
# logger.setLevel(DEBUG)

parameters = "abcdefghijklmnopqrstuvwxyz"
_primitive = "<primitive>"


class PRF():
    def __init__(self, notation, notation_body, arity, func):
        self.notation = notation
        self.notation_body = notation_body
        self.arity = arity
        self.func = func

    def __call__(self, *args):
        ret = self.func(*args)
        print("# eval: {} = {}".format(self.notation.format(*args), ret))
        return ret

    def __param_str__(self):
        return self.notation.format(*parameters)

    def __str__(self):
        return "{} := {}".format(self.notation.format(*parameters), self.notation_body)


Z = PRF("Z()", "0", 0, lambda: 0)
S = PRF("S({})", "a'", 1, lambda x: x + 1)


def params_str(n):
    return ','.join(["{}"] * n)


def P(n, i):
    return PRF("P^{}_{}({})".format(n, i, params_str(n)), parameters[i-1], n, lambda *args: args[i-1])


def composite(notation, f, gs):
    assert isinstance(f, PRF), all(map(lambda g: isinstance(g, PRF), gs))
    assert len(gs) > 0
    g_arity = gs[0].arity

    def h(*xs):
        arguments = map(lambda g: g(*xs), gs)
        return f(*arguments)
    return PRF(notation, notation_body="", arity=g_arity, func=h)


def recursion(notation, f, g):
    def h(x, *ys):
        f(*ys) if x == 0 else g(x-1, h(x-1, *ys), *ys)
    return PRF(notation, "", h)


logger.debug('primrec loaded.')
