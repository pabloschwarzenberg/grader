rut = int(input("Ingrese su rut sin dígito verificador: "))

#definición de cifras

cifra1 = rut%10

rut = rut - cifra1

cifra2 = (rut%100)/10

rut = rut-cifra2*10

cifra3 = (rut%1000)/100

rut = rut - cifra3*100

cifra4 = (rut%10000)/1000

rut = rut - cifra4*1000

cifra5 = (rut%100000)/10000

rut = rut - cifra5*10000

cifra6 = (rut%1000000)/100000

rut = rut - cifra6*100000

cifra7 =(rut%10000000)/1000000

rut = rut - cifra7*1000000

cifra8 = (rut%100000000)/10000000

#multiplicar digitos

mult1 = cifra1*2
mult2 = cifra2*3
mult3 = cifra3*4
mult4 = cifra4*5
mult5 = cifra5*6
mult6 = cifra6*7
mult7 = cifra7*2
mult8 = cifra8*3

#suma de productos

sumaProductos = mult1 + mult2 + mult3 + mult4 +mult5 +mult6 +mult7 +mult8

result = sumaProductos/11
resultadoTruncado = int(result)

result2 = resultadoTruncado*11

#digito verificador

digVerificador1 = sumaProductos - result2

digVerificador = 11 - digVerificador1

if digVerificador == 11:
    digVerificador = 0
elif digVerificador == 10:
    digVerificador = 'K'

print("dv", digVerificador, sep='=')
