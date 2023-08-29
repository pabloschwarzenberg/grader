#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
while not (numero>=10000000 and numero <= 99999999):
    numero = int(input("Ingrese numero telefonico: "))

hora = int(input("Ingrese hora de la llamada: "))
while not(hora>=0 and hora<=23):
    hora = int(input("Ingrese hora de la llamada: "))

ultimosDigitos = numero%1000
primerosDigitos = numero//100000
if (hora>=0 and hora<=7):
    print("CONTESTAR")
elif(hora<14):
    if ultimosDigitos==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif(hora>=17 and hora<=19):
    print("CONTESTAR")
    if primerosDigitos == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")
    