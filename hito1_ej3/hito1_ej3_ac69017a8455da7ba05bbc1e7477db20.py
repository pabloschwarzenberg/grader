ingreso = int(input("Digite sus ingresos en pesos:"))
nacimiento = int(input("Ingrese el año de su nacimiento: "))
hijos = int(input("¿Cuantos hijos tiene: "))
antiguedad = int(input("Años de pertenencia al banco: "))
estado_civil = input("Soltero (S) o Casado (C): ")
vivienda = input("Urbano (U) o Rural (R):")
edad = 2022 - nacimiento
#Condicion 1 = Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos. ok

if antiguedad >10 and hijos >=2:
    print("APROBADO")

#Condicion 2 = Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años


elif estado_civil =="C" and hijos >3 and edad >=45 and edad <=55 :
    print("APROBADO")



#Condición 3 = Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad. Ok
 
elif  ingreso > 2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")


#Condicion 4 = Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años

elif ingreso >3499999 and antiguedad >5:
    print("APROBADO")

#Condicion 5 = Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif vivienda =="R" and estado_civil =="C" and hijos ==1:
    print("APROBADO")
else:
    print("RECHAZADO")


