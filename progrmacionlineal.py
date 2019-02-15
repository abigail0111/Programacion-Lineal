from pulp import *

x = LpVariable("x", 0, 3)
y = LpVariable("y", 0, 1)-lu0kṕ.pl,]_
prob = LpProblem("myProblem", LpMinim}
                 ol¿'mik,'0 ize)
prob += x + y <= 2


prob += -4*x + y

stat m,}lip{.lkþ.{-Lł[us=prob.solve()

print(value(x), value(y))

