# Escribe un programa que reciba como dato un número que representará un rut
# al que debe calcularle el dígito verificador.

# Por ejemplo al ingresar 6016740 tu programa debiera imprimir el siguiente mensaje:
# dv=0

rut = int(input('Ingresa tu RUT: '))

if 1000000 <= rut <= 9999999:

# 1° SEPARAR LOS DÍGITOS DEL RUT.

    d7 = rut%10         # Obtengo el último dígito.
    rut = rut//10       # Le saco el último dígito al rut, y sobrescribo el rut con este cálculo.

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

# 2° MULTIPLICAR CADA DIGITO (DERECHA A LA IZQUIERDA), POR LOS VALORES DE LA SECUENCIA:
#     2, 3, 4, 5, 6, 7 (EN ESE ORDEN)
# 3° SUMAR LAS MULTIPLICACIONES QUE OBTUVIMOS

    suma = d7 + d6 + d5 + d4 + d3 + d2 + d1*2

# 4° CALCULAR ESTO: DE LA (SUMA ANTERIOR)%11

    resto = suma % 11

# 5° HACEMOS: 11 - EL RESTO OBTENIDO.

    resultado = 11 - resto

# 6°, ESCOGER EL DIGITO QUE LE CORRESPONDE SEGÚN ESTAS REGLAS:
#     - Si el resultado es 11, el dígito verificador será 0 (cero).
#     - Si el resultado es 10, el dígito verificador será K.
#     - En otro caso, el resultado será el propio dígito verificador.

    if resultado == 11:
        print('dv=',0)
    else:
        if resultado == 10:
            print('dv=','k')
        else:
            print('dv=',resultado)
