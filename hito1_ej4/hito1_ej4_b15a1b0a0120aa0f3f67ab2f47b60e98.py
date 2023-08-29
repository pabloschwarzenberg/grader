#Conversión de Decimal a Binario

#ENTRADA

n = int(input("ingrese un numero decimal: "))
bi = ""

#DESARROLLO

while n > 0:
    resto = n % 2
    n = n // 2
    bi = str(resto) + bi
    

#SALIDA

print("resultado = " + bi)