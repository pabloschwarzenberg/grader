#Contestador de celular
 numero = int(input("Ingrese el numero telefonico(8 digitos): "))
hora = int(input("Ingrese la hora de la llamada: "))


n = str(numero)[5:8]
m = str(numero)[0:3]

if hora <= 0 and hora <= 7:
    print("contesta")
if hora <= 14 and n == "909":
    print("Contesta")
if hora >= 17 and hora <= 19:
    print("Contesta")
if hora >= 17 and hora <= 19 and m == "877":
    print("no contestar")
if hora > 19:
    print("no Contestar")     