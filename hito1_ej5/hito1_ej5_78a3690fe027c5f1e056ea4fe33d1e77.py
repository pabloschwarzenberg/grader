#Cálculo del dígito verificador de un rut
#Entrada de datos
rut = int(input("Ingrese su RUT sin puntos y sin el digito verificador: "))

#Procesamiento de datos
#8 digitos
if len(str(rut)) == 8:
    digito1 = rut%10
    digito2 = (rut%100)//10
    digito3 = (rut%1000)//100
    digito4 = (rut%10000)//1000
    digito5 = (rut%100000)//10000
    digito6 = (rut%1000000)//100000
    digito7 = (rut%10000000)//1000000
    digito8 = rut//10000000

#Calculo de Digito Verificador
    resultado1 = digito1 * 2
    resultado2 = digito2 * 3
    resultado3 = digito3 * 4
    resultado4 = digito4 * 5
    resultado5 = digito5 * 6
    resultado6 = digito6 * 7
    resultado7 = digito7 * 2
    resultado8 = digito8 * 3
    sumaResultados = resultado1 + resultado2 + resultado3 + resultado4 + resultado5 + resultado6 + resultado7 + resultado8
    resto = sumaResultados%11
    digitoVerificador = 11 - resto
    if digitoVerificador == 11:
        digitoVerificador = 0
    if digitoVerificador == 10:
        digitoVerificador = "K"

#7 digitos
if len(str(rut)) == 7:
    digito1 = rut%10
    digito2 = (rut%100)//10
    digito3 = (rut%1000)//100
    digito4 = (rut%10000)//1000
    digito5 = (rut%100000)//10000
    digito6 = (rut%1000000)//100000
    digito7 = (rut%10000000)//1000000

#Calculo de Digito Verificador
    resultado1 = digito1 * 2
    resultado2 = digito2 * 3
    resultado3 = digito3 * 4
    resultado4 = digito4 * 5
    resultado5 = digito5 * 6
    resultado6 = digito6 * 7
    resultado7 = digito7 * 2
    sumaResultados = resultado1 + resultado2 + resultado3 + resultado4 + resultado5 + resultado6 + resultado7
    resto = sumaResultados%11
    digitoVerificador = 11 - resto
    if digitoVerificador == 11:
        digitoVerificador = 0
    if digitoVerificador == 10:
        digitoVerificador = "K"
print("dv=", digitoVerificador)