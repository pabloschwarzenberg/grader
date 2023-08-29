#Ordenar tres números
      numero_1=int(input("ingresar un numero:"))
numero_2=int(input('ingresar un numero:'))
numero_3=int(input('ingresar un numero:'))

if    numero_1>=numero_2 and numero_1>=numero_3:
    print (numero_1)
elif numero_1<=numero_2:
    print(numero_2)
elif numero_1<=numero_3:
        print(numero_3)

if numero_2>=numero_1 and numero_2>=numero_3:
    print(numero_2)
elif numero_2<=numero_1:
    print(numero_1)
elif numero_2<=numero_3:
    print(numero_3)
 
if numero_3>=numero_1 and numero_3>=numero_2:
    print(numero_3)
elif numero_3<=numero_1:
    print(numero_1)
elif numero_3<=numero_2:
    print(numero_2)
