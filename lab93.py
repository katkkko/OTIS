T={"чорнобривці: Україна","м'ята: Україна","ромашка: Україна","імбир: Україна","лаванда: Україна","баобаб: Африка", "какао: Африка", "Вельвічія: Африка"} 
#створення словника
T1={} #порожній словник, який буде заповнюватися назвою та перекладом
for i in T: #початок циклу Т, і бере значення ключів
  T1[i]=input(i+ "_переклад:") #заповнення другого словника, беручи елементи з першого словника
print(T) #вивести Т
print(T1)#вивести Т1
