from array import *  # створення порожнього масиву цілих чисел 
masiv1=array('i',[]) #створення масиву
for i in range(0,7,1):  #вивід значень в середині функції 
 ss="num"+str(i+1)+":" 
 N=int(input(ss)) #послідовні номери
 masiv1.append(N) 
for j in range(0,7,1):   
 N1=masiv1[j] 
 for l in range(1,N1+1,1): 
   if (N1%l)==0: 
    print(l, end=' ') 
 print("")