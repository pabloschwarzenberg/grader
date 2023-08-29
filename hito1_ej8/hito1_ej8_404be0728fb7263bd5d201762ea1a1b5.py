#Descomponer un número
Numero = int(input("Escriba un numero de hasta cuatro digitos: "))
u = Numero % 10
d = int((Numero % 100) / 10)
c = int((Numero % 1000) /100)
m = int((Numero - (Numero % 1000)) /1000)

contador = len(str(Numero))
if contador == 4:
    print(m,"M +",c,"C +",d,"D +",u,"U")
if contador == 3:
    print(c,"C +",d,"D +",u,"U")
if contador == 2:
    print(d,"D +",u,"U")
if contador == 1:
    print(u,"U")

      