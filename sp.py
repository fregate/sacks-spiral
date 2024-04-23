# API for Saks prime spiral generation
# 1. Spiral Step in millimeters
# 2. Arc width
# 3. Arc color
# 4. Bubble color
# 5. Bubble font?
# 6. Origin size in mm (square file)

# https://docs.sympy.org/latest/modules/ntheory.html
# https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.primefactors

# >>> from sympy import sieve, prime
# >>> print([i for i in sieve.primerange(19)])
# [2, 3, 5, 7, 11, 13, 17]


########################


# from pyx import *
# from math import *
       
# n = 10000    
# ca = canvas.canvas()

# for j in range(n):   
#     i = j + 1
#     r = sqrt(i)
#     theta = r * 2 * pi  
#     x = cos(theta)*r
#     y = -sin(theta)*r        
#     factors = factor(i)               
#     if(len(factors)>1):            
#         radius = 0.05*pow(2,len(factors)-1)
#         ca.fill(path.circle(x,y, radius))
                              
                              
# d = document.document(pages = [document.page(ca, 
#                      paperformat=document.paperformat.A4, fittosize=1)])
# d.writePSfile("spiral_simple.ps")
