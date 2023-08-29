#Contestador de celular
telefono=int(input("Ingrese numero telefonico: "))
while not(telefono>= 10000000 and telefono<=99999999):
    telefono=str(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
while not(hora>=0 and hora<=23):
    hora=int(input("Ingrese hora de la llamada: "))


ultimosDigitos = str(telefono)[5:8]
primerosDigitos = str(telefono)[:3]

ultimosDigitos=int(ultimosDigitos)
primerosDigitos=int(primerosDigitos)

if hora>=0 and hora<=7:
    resultado = "CONTESTAR"

elif hora<14:
    if ultimosDigitos==909:
        resultado = "CONTESTAR"
    else:
        resultado = "NO CONTESTAR"

elif hora>=17 and hora<=19:
    resultado = "CONTESTAR"
    if primerosDigitos==877:
        resultado = "NO CONTESTAR"

else:
    resultado= "NO CONTESTAR"

print(resultado)

