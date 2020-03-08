def doctest_godel_beta():
    """doctest for qiita article
>>> #from functools import partial
>>> #from itertools import repeat, islice, count, combinations, starmap
>>> #from operator import mul
>>> import numpy as np
>>> from sympy.ntheory.modular import crt

>>> a = [31, 5, 51, 0, 2]
>>> a
[31, 5, 51, 0, 2]
>>> n = len(a)
>>> n
5

>>> a_ = np.array(a)
>>> a_
array([31,  5, 51,  0,  2])

>>> a_idx = np.arange(n)
>>> a_idx
array([0, 1, 2, 3, 4])

>>> m0 = np.lcm.reduce(a_idx[1:])
>>> m0
12

>>> def m_i_seq(m): return (a_idx + 1) * m + 1

>>> mis = m_i_seq(12)
>>> mis
array([13, 25, 37, 49, 61])

>>> a_ < mis
array([False,  True, False,  True,  True])

>>> mis = m_i_seq(24)
>>> mis
array([ 25,  49,  73,  97, 121])
>>> a_ < mis
array([False,  True,  True,  True,  True])

>>> mis = m_i_seq(36)
>>> mis
array([ 37,  73, 109, 145, 181])
>>> a_ < mis
array([ True,  True,  True,  True,  True])

>>> np.gcd.outer(mis, mis)
array([[ 37,   1,   1,   1,   1],
       [  1,  73,   1,   1,   1],
       [  1,   1, 109,   1,   1],
       [  1,   1,   1, 145,   1],
       [  1,   1,   1,   1, 181]])

>>> l, M = crt(mis.tolist(), a)
>>> l, M
(mpz(2496662055), 7726764205)

>>> np.multiply.reduce(mis)
7726764205

>>> decoded = np.mod(l, mis)
>>> decoded 
array([mpz(31), mpz(5), mpz(51), mpz(0), mpz(2)], dtype=object)
>>> a_
array([31,  5, 51,  0,  2])

>>> decoded[1] * 6
mpz(30)
    """
    return None

import doctest
doctest.testmod()
