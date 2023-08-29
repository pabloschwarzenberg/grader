# Contestador de celular
# Entrada

n=int(input("Ingrese numero de telefono: "))
hora=int(input("ingrese hora:  "))

# Procesamiento

if hora >= 24 or hora < 0:
    print("la hora debe ser un numero entre 0 y 23")
elif n <= 10000000 or n >= 99999999:
    print("debe ser un numero de 8 digitos")
else:
    ultimo = n % 1000
    if hora > 19:
        print("NO CONTESTAR")
    elif  hora > 0 and hora < 7:
        print("CONTESTAR")
    elif hora > 7 and hora < 14 and ultimo == 909:
       print("CONTESTAR")
    elif hora > 17 and hora < 19 and not ultimo == 877:
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")