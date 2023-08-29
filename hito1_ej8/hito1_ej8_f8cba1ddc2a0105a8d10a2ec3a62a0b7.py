#Descomponer un número
def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10
    return (miles, centenas, decenas, unidades)

numero = int(input("Ingresa un número de hasta 4 dígitos: "))

(miles, centenas, decenas, unidades) = descomponer_numero(numero)

descomposicion = ""
if miles > 0:
    descomposicion += str(miles) + "M + "
if centenas > 0:
    descomposicion += str(centenas) + "C + "
if decenas > 0:
    descomposicion += str(decenas) + "D + "
if unidades > 0:
    descomposicion += str(unidades) + "U"
if descomposicion.endswith(" + "):
    descomposicion = descomposicion[:-3]

print("La descomposición de", numero, "es:", descomposicion)