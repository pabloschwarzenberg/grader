#Cálculo del dígito verificador de un rut
rut = int(input("ingrese su rut: "))
suma = 0
serie = 2
contador = 8
decimo = 10
equis = 1
while contador != 0:
    digito = rut%decimo
    multiplicacion = serie*digito
    multiplicacion = multiplicacion//equis
    rayos = multiplicacion
    rut = rut - digito
    serie = serie + 1
    contador = contador - 1
    decimo = decimo * 10
    equis = equis*10
    total = multiplicacion + suma
    suma = total
    
    if serie == 8:
        serie = 2
    
modulo = total//11

modulox = modulo*11

numero = total - modulox 

verif = 11 - numero

if verif <= 9:
    print("dv=", verif)
elif verif == 10:
    print("dv=K")
else:
    print("dv=0")
    
      