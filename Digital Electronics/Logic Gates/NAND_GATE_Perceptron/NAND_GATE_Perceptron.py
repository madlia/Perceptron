"""
NAND Gate Using Perceptron

NAND Gate is combination of AND Gate and Not Gate
NAND = AND + NOT

 a b A y'
 0 0 0 1 
 0 1 0 1
 1 0 0 1
 1 1 1 0

"""

from AND_GATE_Perceptron import perceptron as AND
from NOT_GATE_Perceptron import perceptron as NOT

input = [1,0]
print("AND Gate Output For "+ str(input) + " : " + str(AND(input)))
print("NOT Gate Output For "+ str(1) + " : " + str(NOT(1)))

print("NAND Gate Output For "+ str(input) + " : " + str(NOT(AND(input))))
