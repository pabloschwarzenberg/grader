import random
num=int(input(""))
a=random.randint(1,20)
i=1
while i<=5:
    if num!=a:
        if num>a:
            print("mi número es menor")
            
            if num==a:
              print("Adivinaste mi número era",a)
        else:
            print("mi número es mayor")
            
            if num==a:
              print("Adivinaste mi número era",a)
        if i==5:
            print("No adivinaste mi número era",a)
    else:
        print("Adivinaste mi número era",a)
    i+=1
        

