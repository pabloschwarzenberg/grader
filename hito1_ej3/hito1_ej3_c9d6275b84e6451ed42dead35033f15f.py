#Datos del cliente
ingresos=int(input("Ingresos : "))
año_cliente=int(input("Ingrese su año de nacimiento: "))
numero_hijos=int(input("Ingrese su numero de hijos : "))
año_perte=int(input("Ingrese el numero de años al que ha pertenecido al banco :"))
estado=(input("Ingrese su estado civil ((s)si es soltero , (c)si es casado): "))
vivienda=(input("Ingrese su tipo de vivienda ((U) si es urbana,(R) si es rural: "))
#Ecuaciones
Edad = 2020-año_cliente
#Condiciones
if año_cliente > 10 and numero_hijos >= 2:
    print("APROBADO")
    
if estado=="c" or estado=="C" and numero_hijos > 3 and 45 <= Edad <= 55 :
    print("APROBADO")

if ingresos > 3500000 and año_perte > 5 :
    print("APROBADO")
    
if ingresos > 2500000 and estado=="s" or estado=="S" and vivienda == "U" or vivienda == "u" :
    print("APROBADO")

if estado=="c" or estado=="C" and  vivienda == "R" or vivienda == "r" and numero_hijos < 2 :
    print("APROBADO")

else : print("RECHAZADO")    

