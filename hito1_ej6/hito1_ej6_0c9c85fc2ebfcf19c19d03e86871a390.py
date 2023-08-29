#Ordenar tres números
nro1 = int(input("ingrese nro 1: "))
nro2 = int(input("ingrese nro 2: "))
nro3 = int(input("ingrese nro 3: "))

sumatoria = nro1+nro2+nro3

if nro1 > nro2 and nro1 > nro3:
    mayor = nro1
elif nro2 > nro1 and nro2 > nro3:
    mayor = nro2
else:
    mayor = nro3

if nro1 < nro2 and nro1 < nro3:
    menor = nro1

elif nro2 < nro1 and nro2 < nro3:
    menor = nro2

else:
    menor = nro3
mediano=sumatoria - (mayor+menor)

print(str(menor) +","+ str(mediano)+","+ str(mayor))