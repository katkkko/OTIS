import numpy
import random

s = input()
s = s.split()
n = int(s[0])
m = int(s[1])

A = numpy.empty((n, m))
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = random.randint(0, 1)
print(A)
A = numpy.c_[A, numpy.zeros(m)]
print()
for i in range(len(A)):
    A[i][-1] = 0
for i in range(len(A)):
    if (A[i].sum()) % 2 != 0:
        A[i][-1] = 1

print(A)