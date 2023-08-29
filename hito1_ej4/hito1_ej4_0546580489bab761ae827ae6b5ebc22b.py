#Conversión de Decimal a Binario
n = int(input("INGRESE EL NUMERO A CONVERTIR: "))
bi = ""
while n >= 1:
    if round(n % 2) == 1:
        bi = bi + "1"
        n = int(n / 2)
        print("primer if:", n)
    elif round(n % 2) == 0:
        bi = bi + "0"
        n = int(n / 2)
        print("el elif: ", n)
    else:
        break

bi = bi[::-1]
print("resultado={0}".format(bi))

      