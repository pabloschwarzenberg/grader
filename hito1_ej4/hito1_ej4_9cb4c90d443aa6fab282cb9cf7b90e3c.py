#Conversión de Decimal a Binario
 
nDecimal= int(input("Ingrese el número decimal: "))
datos = []
string = ""

while nDecimal > 0:
    binari = nDecimal % 2
    nDecimal = nDecimal // 2
    datos.append(binari) 
contador = 0
datos.reverse()

while contador < len(datos):
    string = string + str(datos[contador])
    contador = contador + 1

print("resultado=", string) 