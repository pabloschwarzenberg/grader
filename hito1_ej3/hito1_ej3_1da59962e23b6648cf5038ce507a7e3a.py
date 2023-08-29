#Aprobación de créditos
while True:
    ingreso=int(input("Complete con sus ingresos en pesos: "))
    if ingreso>=0:
        break
    else:
        print("Ingrese un número valido")
while True:        
    nacimiento=int(input("Ingrese su año de nacimiento: "))
    if nacimiento>=0:
        break
    else:
        print("Ingrese un número valido")
while True:        
    hijos=int(input("¿Cuantos hijos tiene? :"))
    if hijos>=0:
        break
    else:
        print("Ingrese un número valido")
while True:        
    antiguedad=int(input("¿Cuantos años lleva en el banco? :"))
    if antiguedad>=0:
        break
    else:
        print("Ingrese un número valido")
while True:     
    estado=str(input("Ingrese S si es soltero/a o C si es casado/a: "))
    if estado=="S" or estado=="C":
        break
    else:
        print("Ingrese una respuesta valida")
while True:
    vivienda=str(input("Ingrese U si vive en un lugar urbano o R si vive en un lugar rural: "))
    if vivienda=="U" or vivienda=="R":
        break
    else:
        print("Ingrese una respuesta valida")
edad=2022-nacimiento
if antiguedad>10 and hijos>=2:
    print("APROBADO")
elif estado=="U" and hijos>3 and 55>edad>45:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vivienda=="U":
    print("APROBADO")
elif ingreso>3500000 and antiguedad>5:
    print("APROBADO")
elif vivienda=="R" and estado=="C" and 2>hijos:
    print("APROBADO")
else:
    print("RECHAZADO")      