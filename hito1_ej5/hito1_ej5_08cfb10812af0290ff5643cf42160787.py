    
rut = str(input(""))
contador = 2
suma = 0
for i in range(len(rut)):
    if contador > 7:
        contador = 2
    numero = rut[len(rut)- i - 1]
    multiplicacion = contador * int(numero)
    suma += multiplicacion
    contador += 1

final = 11 - suma%11
if final == 11:
    final = 0
if final == 10:
    final = ("k")
print("dv=" + str(final))




