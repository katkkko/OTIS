import math
def f(x):
      y=float(math.e**2+(math.fabs(x)**1/2))
      return(y)
a=float(input("значення a"))
b=float(input("значення b"))
h=float(input("значення h"))
b1=int(round(b))
sp=[]
x1=a
i=a
for i in range(b1+1):
    sp.append(f(x1))
    print(f(x1))
    x1=x1+h
    if x1>b :
        break
print("найменше значення", min(sp))
print (sp)