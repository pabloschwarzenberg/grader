#Ordenar tres números
#Entrada de datos
nro1 = int(input("Ingrese un numero: "))
nro2 = int(input("Ingrese otro numero: "))
nro3 = int(input("Ingrese un numero mas: "))
nroMayor = 0
nroMenor = 0
nroMedio = 0

#Procesamiento de datos
#Numeros iguales
if nro1 == nro2 and nro2 > nro3:
    nroMenor = nro3
    nroMedio = nro1
    nroMayor = nro2
if nro1 == nro3 and nro1 > nro2:
    nroMenor = nro2
    nroMedio = nro1
    nroMayor = nro3
if nro2 == nro3 and nro2 > nro1:
    nroMenor = nro1
    nroMedio = nro2
    nroMayor = nro3
if nro1 == nro2 and nro2 < nro3:
    nroMenor = nro2
    nroMedio = nro1
    nroMayor = nro3
if nro1 == nro3 and nro1 < nro2:
    nroMenor = nro3
    nroMedio = nro1
    nroMayor = nro2
if nro2 == nro3 and nro2 < nro1:
    nroMenor = nro3
    nroMedio = nro2
    nroMayor = nro1
#Numero mayor
if nro1 > nro2 and nro1 > nro3:
    nroMayor = nro1
if nro2 > nro1 and nro2 > nro3:
    nroMayor = nro2
if nro3 > nro1 and nro3 > nro2:
    nroMayor = nro3
#Numero menor
if nro1 < nro2 and nro1 < nro3:
    nroMenor = nro1
if nro2 < nro1 and nro2 < nro3:
    nroMenor = nro2
if nro3 < nro1 and nro3 < nro2:
    nroMenor = nro3
#Numero del medio
if nroMayor > nro1 > nroMenor:
    nroMedio = nro1
if nroMayor > nro2 > nroMenor:
    nroMedio = nro2
if nroMayor > nro3 > nroMenor:
    nroMedio = nro3

#Salida de datos
print("Los numeros ordenaros de menor a mayor son:", nroMenor,",", nroMedio,",", nroMayor)