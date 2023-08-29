#Descomponer un número
def descom_numero(numero):
    u = numero% 10
    d = (numero// 10) % 10
    c = (numero// 100) % 10
    mil = (numero// 1000) % 10
    #separar los valores por miles, centenas, decimales y unidades (u,d,c,m)

    descomposicion = ""

    if mil:
        descomposicion += str(mil) + "M"
    if c:
        descomposicion += str(c) + "C"
    if d:
        descomposicion += str(d) + "D"
    descomposicion += str(u) + "U"

    return descomposicion
#colocar los condicionales en el caso que exista miles, centenas, decimales y/o unidades lo imprima el programa



numero = int(input("Ingrese un numero de hasta 4 digitos: "))
#preguntar el numero que se desea descomponer

descomposicion = descom_numero(numero)
#darle valor a la variable para que de el resultado

print(descomposicion)
#imprimir el resultado
