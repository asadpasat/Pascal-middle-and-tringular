"""finding number that appears in both sequences of
middle number and triangular number
"""
import math

person = input("what is your high band?")

#triangular numbers
def trig(x): return ((x**2 + x)/2)
a= map(trig, range(1,person))

#middle numbers
def mid(z): return ((math.factorial(z))/(math.factorial(z/2)**2))
b = map(mid, range (0,person,2))
#IF YOU WANT YOU CAN UNCOMMENT TETRAHEDRAL NUMBER AND COMMENT TRIANGULAR NUMEBERS AND COMPARE THE INTED
# SAME FOR PENTATOPE? 5th diagonal
#tetrahedral numbers
#def tetra(c): return (((c**3) + 3*(c**2) + (2*c))/ 6)
#c = map(tetra, range (1,person))

#pentatope numbers 
#def penta(v): return ((v(v+1)(v+2)(v+5))/2)
#v = map(penta, range (1,person))

print(([i for j, i in zip(a,c) if i == j]))
