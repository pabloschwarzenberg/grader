import random
a=int((random.randint(1,20)))
i=0
while(i<=5):
    i=i+1
    b=int(input('ingrese numero'))
    if b<a :
       print('el numero es mayor')
    if b>a:
        print('el numero es menor')
    elif (i>=5):
        print("No adivinaste, mi número era ", a)
    if b==a:
        print("Adivinaste, mi número era",a)
        i=i+5