import random

num = random.randrange(20)
contador=1
num2 = int(input("Ingrese su número : "))
while num<num2 or num2<num:
    if num<num2:
        
        print("mi número es menor")
        num2 = int(input("Ingrese su número : "))
        contador+=1
        
    else:
        
        print("mi número es mayor")
        num2 = int(input("Ingrese su número : "))
        contador+=1
    
    if contador==5:
        print("No adivinaste, mi número era " , num)
        break
    if num2==num:
        print("Adivinaste, mi número era " , num)
        break