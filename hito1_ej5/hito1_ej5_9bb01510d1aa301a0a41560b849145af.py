## HITO 1, Ejercicio 7: Cálculo del dígito verificador del rut

# Escribe un programa que reciba como dato un número que representará un rut
# al que debe calcularle el dígito verificador.

# Por ejemplo al ingresar 6016740 tu programa debiera imprimir el siguiente mensaje:
# dv=0

# link: es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario


rut = int(input('Ingresa tu RUT: '))

# 1° Debo separar cada digito del RUT, de derecha a izquierda.

d8 = rut%10          #con %, accedo al último digito de rut. Pero no se lo saco.    
rut = rut//10        #con // le quito, el último dígito, y SOBREESCRIBO en rut. 

d7 = rut%10
rut = rut//10

d6 = rut%10
rut = rut//10

d5 = rut%10
rut = rut//10

d4 = rut%10
rut = rut//10

d3 = rut%10
rut = rut//10

d2 = rut%10
rut = rut//10

d1 = rut%10

##2° Debo multiplicar por los numeros 2,3,4,5,6,7. Si se me acaban, volver a empezar.
##3° Debo sumar las multiplicaciones q obtuve.

suma = d8*2 + d7*3 + d6*4 + d5*5 + d4*6 + d3*7 + d2*2 + d1*3

##4° Debo calcular esto: (suma anterior)%11 (esto me da el resto de dividir por 11!!!!)

resto = suma%11

##5° Ahora debo hacer: 11 - resto del paso anterior.

resultado = 11 - resto

##6° Ahora analizo ese resultado:

##    a. Si el resultado es 11, el dígito verificador será 0 (cero).
if resultado == 11:
    print('dv=0')

##    b. Si el resultado es 10, el dígito verificador será K.
if resultado == 10:    
    print('dv=K')

##    c. En otro caso, el resultado será el propio dígito verificador.
if resultado != 10 and resultado != 11:
    print('dv=', resultado)
