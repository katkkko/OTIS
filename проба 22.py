import math 
x= float(input("x:")) 
def func(x): 
    if x >=3.86: 
        return (math.sqrt (2,25*x**2+math.log10(math.fabs (x)))) 
    elif 1.54< x : 
        return (math.e**x+(12*x**2-1)/x+9) 
    else:  
        return (math.log1p(math.fabs(x))-x**x) 
 
print(func(x))