#Aprobación de créditos
ingreso = int(input("Ingrese la cantidad que ingresos que tiene(pesos): "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese cuantos hijos tiene: "))
añosBanco = int(input("Ingrese hace cuantos años pertenece al banco: "))
estadoCivil = input("Ingrese si esta casado(C) o soltero(S): ")
vivienda = input("Ingrese si vive en campo(R) o ciudad(U): ")

fecha = 2020
edad = (fecha - nacimiento)

if (añosBanco>=10 and hijos>=2) or (estadoCivil=="C" and hijos>3 and (edad<55 or edad>45)) or \
   (ingreso>2500000 and estadoCivil=="S" and vivienda=="U") or (ingreso>3500000 and añosBanco>5) or \
   (vivienda=="R" and estadoCivil=="C" and hijos<2):
    print("APROBADO")  