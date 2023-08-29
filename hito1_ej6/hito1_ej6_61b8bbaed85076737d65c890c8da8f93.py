#Ordenar tres números
print("Ordenador de 3 numeros de menor a mayor")
Numero1=int(input("ingresa el primer numero"))
Numero2=int(input("ingresa el segundo numero"))
Numero3=int(input("ingresa el tercer numero"))
if Numero3<Numero1:
   print(Numero1,",",Numero3)
if Numero2<Numero3:
   print(Numero3,",",Numero2)
if Numero1<Numero2:
   print(Numero2,",",Numero1)