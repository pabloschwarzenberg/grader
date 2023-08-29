#Ordenar tres números
primerNumero  =  int ( input ( "Primer Numero:" ))
segundoNumero  =  int ( input ( "Segundo Numero:" ))
tercerNumero  =  int ( input ( "Tercer Numero:" ))
mayor, mediano, menor = 0,0,0
if primerNumero > segundoNumero and primerNumero > tercerNumero:
    mayor = primerNumero
    if segundoNumero > tercerNumero:
        mediano, menor = segundoNumero, tercerNumero
    else:
        mediano, menor = tercerNumero, segundoNumero
if segundoNumero > primerNumero and segundoNumero > tercerNumero:
    mayor = segundoNumero
    if primerNumero > tercerNumero:
        mediano, menor = primerNumero , tercerNumero
    else:
        mediano, menor = tercerNumero, primerNumero
elif tercerNumero > primerNumero and tercerNumero > segundoNumero:
    mayor = tercerNumero
    if primerNumero > segundoNumero:
        medio, menor = primerNumero, segundoNumero
    else:
        medio, menor = segundoNumero, primerNumero

print("El mayor de los tres numeros es:", mayor)
print("El medio de los tres numeros es:", mediano)
print("El menor de los tres numeros es:", menor)