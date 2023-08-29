#Cálculo del dígito verificador de un rut

# link: es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario

# Ejemplo Wiki: 30686957-4

rut = int(input('Ingresa tu rut sin dígito verificador: '))

# 1° Tomar los dígitos del RUT por separado, de derecha a izquierda.

d1 = rut%10   # Con %10 Conseguimos el último dígito
rut = rut//10  # Con //10 le sacamos al rut el último dígito. Se sobreescribe rut.

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

# 2° Multiplicar cada dígito por los números 2, 3, 4, 5, 6, 7. Si se acaban, partir
# con el 2 de nuevo.
# 3° Sumar los resultados que obtuvimos. (valor de wiki 194)

suma = d1*2 + d2*3 + d3*4 + d4*5 + d5*6 + d6*7 + d7*2 + d8*3 

# 4° Calcular el resto de la suma anterior con 11 (calcular esto: %11) (valor de wiki 7)

resto = suma%11

# 5° Hacer esta resta: 11 - resto del punto anterior. (valor de wiki 4)

resultado = 11 - resto

# 6° Analizar el resultado anterior:
#     a. Si el resultado es 11, el dígito verificador será 0 (cero).
if resultado == 11:
    print('dv=0')

#     b. Si el resultado es 10, el dígito verificador será K.
if resultado == 10:
    print('dv=K')
   
#     c. En otro caso, el resultado será el propio dígito verificador.
if resultado != 11 and resultado != 10:

    dvSinEspacio = 'dv=' + str(resultado)
    print(dvSinEspacio)
    print('dv=', resultado)      