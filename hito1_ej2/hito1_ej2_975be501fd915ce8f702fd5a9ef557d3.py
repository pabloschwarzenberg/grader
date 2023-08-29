#Contestador de celular
celular=0
while celular<10000000:
    celular = int(input("Ingrese número telefónico: "))

Hora = int(input("Ingrese hora de la llamada: "))
primero=celular//100000
ultimos=celular%1000


if Hora>= 0 and Hora<= 7:
   print("Resultado: Contestar")
if Hora<14 and ultimos!= 909:
    print("Resultado: No contestar")
if Hora<14 and ultimos == 909:
    print("Contestar")
if Hora>= 17 and Hora<= 19:
    print("Contestar")
if primero == 877:
      print("Resultado:No contestar")
if Hora>19:
     print("Resultado:No contestar")