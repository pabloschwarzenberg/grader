#Contestador de celular
def contestar_celular(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"

    if hora < 14:
        if numero % 1000 == 909:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"

    if hora >= 17 and hora < 19:
        if str(numero)[0:3] != "877":
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"

    return "NO CONTESTAR"

# Solicitar el número telefónico y la hora al usuario
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

# Verificar si contestar o no
decision = contestar_celular(hora, numero)

# Imprimir el resultado
print("Resultado:", decision)
     