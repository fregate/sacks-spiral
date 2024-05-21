# API for Saks prime spiral generation
# 1. Spiral Step in millimeters
# 2. Arc width
# 3. Arc color
# 4. Bubble color
# 5. Bubble font?
# 6. Paper size in mm (square file)

# https://docs.sympy.org/latest/modules/ntheory.html
# https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.primefactors

# >>> from sympy import sieve, prime
# >>> print([i for i in sieve.primerange(19)])
# [2, 3, 5, 7, 11, 13, 17]


########################


from pyx import *
from math import *
from sympy import divisors
       
n = 10000    
ca = canvas.canvas()

prx = 0
pry = 0
for j in range(n):   
    i = j + 1
    r = sqrt(i)
    theta = r * 2 * pi  
    x = cos(theta) * r
    y = -sin(theta) * r
    factors = divisors(i)
    # factors = factor(i)
    if (len(factors) <= 2):
        ca.fill(path.circle(x, y, 0.5))
    if sqrt(i) == isqrt(i) and i != 1:
        ca.stroke(path.circle(x, y, 0.3))
    if j > 0:
        ca.stroke(path.line(prx, pry, x, y))
        # draw arc from prev to current
        pass
    prx = x
    pry = y

ca.writePDFfile("sp")
