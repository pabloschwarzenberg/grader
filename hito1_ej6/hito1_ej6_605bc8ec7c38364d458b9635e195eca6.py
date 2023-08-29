#Ordenar tres números
Primero= int(input("ingrese el primer numero: "))
Segundo= int(input("ingrese el segundo numero: "))
Tercero= int(input("ingrese el tercer numero: "))
if(Primero<=Segundo<=Tercero):
 print("ordenados de menor a mayor: ",Primero,",",Segundo,",",Tercero)
if(Segundo<=Tercero<=Primero):
 print("ordenados de menor a mayor: ",Segundo,",",Tercero,",",Primero)
if(Tercero<=Primero<=Segundo):
 print("ordenados de menor a mayor: ",Tercero,Primero,Segundo)