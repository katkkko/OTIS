import math
x=1
y=math.e**2+(math.fabs(x)**1/2)
    
a=float(input('first'))
b=int(input('second'))
h=int(input('step'))
x=a
y=0.0
list=[]
for y in range(0,100):
 y=round(y,4)
 list.append(y)
 print(y+1,'   ', x,'  ' , y)
 x=round(x,1)
print(list)


 #𝑓(𝑥)=𝑒௫+ඥ|𝑥|