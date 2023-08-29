#Ordenar tres números
numero1=int(input("ingrese numero1: "))
numero2=int(input("ingrese numero2: "))
numero3=int(input("ingrese numero3: "))
numero11=str(numero1)
numero22=str(numero2)
numero33=str(numero3)
if numero1<=numero2<=numero3:
    print(numero11+','+numero22+','+numero33)
if numero1<=numero3<=numero2:
    print(numero11+','+numero33+','+numero22)
if numero2<=numero3<=numero1:
    print(numero22+','+numero33+','+numero11)
if numero2<=numero1<=numero3:
    print(numero22+','+numero11+','+numero33)
if numero3<=numero2<=numero1:
    print(numero33+','+numero22+','+numero11)
if numero3<=numero1<=numero2:
    print(numero33+','+numero11+','+numero22)