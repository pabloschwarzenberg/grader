## HITO 1, Ejercicio 7: Cálculo del dígito verificador del rut

# Escribe un programa que reciba como dato un número que representará un rut
# al que debe calcularle el dígito verificador.

# Por ejemplo al ingresar 6016740 tu programa debiera imprimir el siguiente mensaje:
# dv=0

# link: es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario

# 30.686.957-X -> debemos conseguir dv=4

rut = int(input('Ingresa tu RUT sin dígito verificador: '))

##1° Separar todos los digitos del rut: desde el último hasta el primero

d1 = rut%10
rut = rut//10

d2 = rut%10
rut = rut//10

d3 = rut%10
rut = rut//10

d4 = rut%10
rut = rut//10

d5 = rut%10
rut = rut//10

d6 = rut%10
rut = rut//10

d7 = rut%10
rut = rut//10

d8 = rut%10
rut = rut//10

print(d1, d2, d3, d4, d5, d6, d7, d8)

##2° Multiplicar cada dígito por 2, 3, 4, 5, 6, y 7. Si se acaban, volver a empezar del 2.
##3° sumar todas las multiplicaciones que obtuvimos.
##4° calcular el resto %11, a la suma q obtuvimos arriba.
##5° hacer esto: 11-resto q obtuvimos arriba.
##6° Analizar la resta anterior:
##    a. Si el resultado es 11, el dígito verificador será 0 (cero).
##    b. Si el resultado es 10, el dígito verificador será K.
##    c. En otro caso, el resultado será el propio dígito verificador.
##2° Multiplicar cada dígito por 2, 3, 4, 5, 6, y 7. Si se acaban, volver a empezar del 2.
##3° sumar todas las multiplicaciones que obtuvimos. (en wikipedia es 194)

suma = d1*2 + d2*3 + d3*4 + d4*5 + d5*6 + d6*7 + d7*2 + d8*3

print('suma: ', suma)

##4° calcular el resto %11, a la suma q obtuvimos arriba. (en wikipedia es 7)

resto = suma%11
print('resto: ', resto)
##5° hacer esto: 11-resto q obtuvimos arriba.

resultado = 11 - resto

##6° Analizar la resta anterior:
##    a. Si el resultado es 11, el dígito verificador será 0 (cero).
if resultado == 11:
    print('dv=0')

##    b. Si el resultado es 10, el dígito verificador será K.
if resultado == 10:
    print('dv=K')

##    c. En otro caso, el resultado será el propio dígito verificador.
if resultado != 11 and resultado != 10:
    print('dv=', resultado)
