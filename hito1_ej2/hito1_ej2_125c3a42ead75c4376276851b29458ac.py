#Contestador de celular
def llamda(numero,hora):
    if hora >= 0 and hora <7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 != 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and numero // 1000000 != 877:
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

numero = int(input("Ingrese el numero: "))
hora = int(input("Ingrese la hroa: "))
resultado = llamda(numero,hora)
print(resultado)