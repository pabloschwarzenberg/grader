import random
a=random.randint(1,20)
intentos=0
e=True
while e:
    b = int(input('adivina el numerillo: '))
    if b==a:
        print("Adivinaste, mi número era ",a)
        break
    else:
        intentos+=1
        if intentos==5:
            e=False
            continue
        if b>a:
            print('es menor')
        elif a>b:
            print('es mayor')
    
print('No adivinaste, mi número era ', a)
          
            