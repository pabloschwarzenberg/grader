#Aprobación de créditos
i= int(input("Indique ¿cuanto es su en ingreso mensual en pesos? : "))
a= int(input("Ingrese su año de nacimiento : " ))
n= int(input("Indique cuantos hijos tiene : " ))
p= int(input("Indique cuantos años a pertenecido a este banco : " ))
e= str(input("¿Cual es su estado civil? 'S' o 'C': "  ))
v= str(input("¿Donde vive usted? 'U' o 'R' : "))
edad = 2020 - a
if p > 10 and n > 2: 
    print("APROBADO")
elif e == "C" and n > 3 and 45 <= edad <= 55:
    print("APROBADO")
elif i >= 2500000 and e == "S" and v == "U":
    print("APROBADO")
elif i >= 3500000 and p > 5:
    print("APROBADO")
elif v == "R" and e == "C" and n < 2:
    print("APROBADO")
else:
    print("RECHAZADO")