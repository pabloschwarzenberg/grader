#Contestador de celular
telefono=(str(input("Ingrese el número telefónico:")))

contador= len(str(telefono))

lista = list(str(telefono))

while contador == 8:
    break
else:
    print(input("Teléfono inválido, por favor ingrese nuevamente su número: "))


hora =(int(input("Ingrese hora de llamada: ")))

if hora in range(0,8):
    print("CONTESTAR EMERGENCIA") 

primerosN = lista[0:3]

if "8"and "7" in lista:
    primerosN = lista[0:3]

if  "8" and "7" in primerosN and hora in range(17,20):
    print("NO CONTESTAR")
elif hora in range(17,20):
    print("CONTESTAR")


ultimosN = lista[5:8]

if "9" and "0" in lista:
    ultimosN = lista[5:8]

if hora in range(8,14) and "9" and "0" in ultimosN:
    print("CONTESTAR")
elif hora in range(8,14):
    print("NO CONTESTAR")


if hora in range(20,24):
    print("NO CONTESTAR") 
    