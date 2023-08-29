#Contestador de celular
cont = 0
while True:
    n = input("Ingrese un numero de telefono de 8 digitos:")
    cont = len(n)
    if cont == 8:
        break

while True:
    hora = int(input("Ingrese la hora del dia: "))
    if hora < 24:
        break

if hora < 8:
    print("CONTESTAR")
elif hora > 7 and hora < 15:
    if n[5:8] == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

elif hora > 16 and hora < 20:
    if n[0:3] == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")