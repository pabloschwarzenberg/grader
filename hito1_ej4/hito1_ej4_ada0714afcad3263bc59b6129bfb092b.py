#Conversión de Decimal a Binario
NUMERO = int(input("Ingresa un numero binario: "))
LISTA = []

while NUMERO > 0:
    RESTO = int(NUMERO%2)
    LISTA.append(RESTO)
    NUMERO = (NUMERO-RESTO)/2
numero_bin = ""

print("esto es: ",LISTA[::-1])

for e in LISTA[::-1]:
    numero_bin = numero_bin + str(e)

print("resultado="+str(numero_bin))      