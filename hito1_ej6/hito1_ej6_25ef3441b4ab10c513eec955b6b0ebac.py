#Ordenar tres números
print("Ordenador de 3 números de menor a mayor")
Número1=int(input("ingresa el primer número: "))
Número2=int(input("ingresa el segundo número: "))
Número3=int(input("ingresa el tercer número: "))
if Número1>=Número2>=Número3:
    print(Número3,",",Número2,",",Número1)
if Número1>=Número3>=Número2:
    print(Número2,",",Número3,",",Número1)
if Número2>=Número1>=Número3:
    print(Número3,",",Número1,",",Número2)
if Número2>=Número3>=Número1:
    print(Número1,",",Número3,",",Número2)
if Número3>=Número2>=Número1:
    print(Número1,",",Número2,",",Número3)
if Número3>=Número1>=Número2:
    print(Número2,",",Número1,",",Número3)