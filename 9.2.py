
S=input("введіть символи:") 
spisok=S.split(' ') 
x=set(spisok) 
print(x) 
a=set() #створення порожньої множини
n=set() 
c=set() 
for i in x: 
    if i.isdigit()==True: #перевіряє чи складається рядок з цифр
        n.add(i) #додавання елемента в множину
    elif i.isalpha()==True: #перевіряє чи складається рядок з літер
        a.add(i) #додавання елемента в множину
    else: #
        c.add(i) #додавання елемента в множину
print(n) 
print(a) 
print(c)