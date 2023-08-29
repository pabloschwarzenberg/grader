#Ordenar tres números
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("ingrese el tercer numero: "))

if numero1>=numero2>=numero3:
    print(numero3,",",numero2,",",numero1)
if numero2>=numero1>=numero3:
    print(numero3,",",numero1,",",numero2)
if numero3>=numero2>=numero1:
    print(numero1,",",numero2,",",numero3)
if numero3>=numero1>=numero2:
    print(numero2,",",numero1,",",numero3)      