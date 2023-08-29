#Ordenar tres números
print ("Progrma para Ordenar tres Numeros")
PrimerNumero = int(input("Ingrese Primer Numero: "))
SegundoNumero = int(input("Ingrese Segundo Numero: "))
TercerNumero = int(input("Ingrese Tercer Numero: "))

if PrimerNumero >= SegundoNumero and PrimerNumero >= TercerNumero and SegundoNumero >= TercerNumero:
    print ("El Orden de los Numeros es: " , TercerNumero , ", " , SegundoNumero , ", " , PrimerNumero )
if PrimerNumero > SegundoNumero and PrimerNumero > TercerNumero and TercerNumero >= SegundoNumero:
    print ("El Orden de los Numeros es: " , SegundoNumero , ", " , TercerNumero , ", " , PrimerNumero )

if SegundoNumero >= PrimerNumero and SegundoNumero >= TercerNumero and PrimerNumero >= TercerNumero:
    print ("El Orden de los Numeros es: " , TercerNumero , ", " , PrimerNumero , ", " , SegundoNumero )
if SegundoNumero >= PrimerNumero and SegundoNumero >= TercerNumero and TercerNumero >= PrimerNumero:
    print ("El Orden de los Numeros es: " , PrimerNumero , ", " , TercerNumero , ", " , SegundoNumero )

if TercerNumero >= PrimerNumero and TercerNumero >= SegundoNumero and PrimerNumero >= SegundoNumero:
    print ("El Orden de los Numeros es: " , SegundoNumero , ", " , PrimerNumero , ", " , TercerNumero )
if TercerNumero >= PrimerNumero and TercerNumero >= SegundoNumero and SegundoNumero >= PrimerNumero:
    print ("El Orden de los Numeros es: " , PrimerNumero , ", " , SegundoNumero , ", " , TercerNumero )