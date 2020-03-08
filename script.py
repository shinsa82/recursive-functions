from sympy.core.compatibility import as_int
from functools import partial
from itertools import repeat, islice, count, combinations, starmap
from operator import mul
import numpy as np
from sympy.ntheory.modular import crt

# sample sequence of length n
a = [31, 5, 51, 0, 2]
n = len(a)
print(a)
print(n)

# convert
a_ = np.array(a)
print(a_)
a_idx = np.arange(n)
print(a_idx)

# compute LCM
m0 = np.lcm.reduce(range(1, n))
print(m0)


def m_i_seq(m): return (a_idx + 1) * m + 1


mis = m_i_seq(12)
print(mis)
print(a_ < mis)

mis = m_i_seq(24)
print(mis)
print(a_ < mis)

mis = m_i_seq(36)
print(mis)
print(a_ < mis)

print(np.gcd.outer(mis, mis))

# l, M = crt([37, 73, 109, 145, 181], [31, 5, 51, 0, 2])
l, M = crt(mis.tolist(), a)
print(l, M)

print(np.multiply.reduce(mis))

decoded = np.mod(l, mis)
print(decoded)
print(decoded.dtype)

print(decoded[1] * 6)

print(list(map(as_int, decoded)))
