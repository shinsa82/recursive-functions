from logging import getLogger, DEBUG
import primrec
from primrec import Z, S, P

logger = getLogger('primrec')
logger.setLevel(DEBUG)

print(Z)
print("arity:", Z.arity)
print(Z())
# print(Z(1)) # error

print(S)
print("arity:", S.arity)
# print(S()) # error
print(S(2))

primrec.params_str(3)

print(P(4, 2))
print(P(4,2).__param_str__())
print("arity:", P(4, 2).arity)
print(P(4, 2)(2, 4, 6, 8))

# add = primrec.recursion("{} + {}", P(1,1), composite)

f1 = primrec.composite("f1", S, [P(3, 2)])
print(f1)
print(f1(2, 4, 6))
