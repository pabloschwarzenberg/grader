from random import randint
a=(randint(1, 20))
print("Tienes 5 intentos")
intentos=4
ganar= False
while intentos <5 and intentos>=0:
    n=int(input("Elige tu número: "))
    if n==a:
        ganar= True
        break
    elif n<=a:
        print("Equivocado el número es mayor al que elegiste")
        print("Intentalo denuevo") 
        
    elif n>=a:
        print("Equivocado el número es menor al que elegiste")
        print("Intentalo denuevo")
    intentos= intentos-1
        
if ganar==False:
    print("No adivinaste, mi número era ",a)
else:
    print("Adivinaste, mi número era ",a)
            