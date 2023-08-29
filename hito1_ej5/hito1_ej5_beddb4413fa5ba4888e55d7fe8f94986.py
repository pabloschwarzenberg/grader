#Cálculo del dígito verificador de un rut
rut = input("Ingrese rut: ")

secuencia = [2, 3, 4, 5, 6, 7]

i = 0
suma = 0
while i < len(rut):
    suma += secuencia[i%len(secuencia)]*int(rut[-i-1])
    i+=1

dv = 11 - suma%11
if dv == 11:
    dv = "0"
elif dv == 10:
    dv = "k"
else:
    dv = str(dv)

print("dv="+dv)
