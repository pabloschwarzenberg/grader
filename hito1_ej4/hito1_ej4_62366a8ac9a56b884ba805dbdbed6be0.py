#Conversión de Decimal a Binario
# Entrada

num = int(input("Ingrese un numero: "))

# Procesamiento

copia = num
residuo = 0
bin = ""

while int(copia) > 0:
    residuo = copia % 2
    copia //= 2
    bin = str(residuo) + str(bin)

print("resultado =", bin)  