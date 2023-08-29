rut = input("Ingrese rut")
listaRut = []


for i in range(len(rut),0,-1):
    a = rut[i-1]
    listaRut.append(a)
   

suma = 0
contador=2

for i in listaRut:
    caracter = int(i)
    suma += caracter*contador
    contador +=1
    if contador == 8:
        contador =2

parte_entera = int(suma/11)
resto = suma - (11*parte_entera)
dv = 11 - resto

if dv == 11:
    dv = 0
if dv == 10:
    dv ="k"

print("dv=",dv)

