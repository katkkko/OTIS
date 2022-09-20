import math
Ox= float(input("Ox:")) 
Oy= float(input("Oy:")) 
Ay= float(input("Ay:")) 
Ax= float(input("Ax:")) 
Ay= float(input("Ay:")) 
Bx= float(input("Bx:")) 
By= float(input("By:")) 
Cx= float(input("Cx:")) 
Cy= float(input("Cy:"))
AO=(Ax,Ay,Ox,Oy)
BO=(Bx,By,Ox,Oy)
CO=(Cx,Cy,Ox,Oy)
if(AO<=BO) and(AO<=CO):
    print("A")
if(BO<=AO) and(CO<=BO):
    print("B")
if(CO<=AO) and(CO<=BO):
    print("C")