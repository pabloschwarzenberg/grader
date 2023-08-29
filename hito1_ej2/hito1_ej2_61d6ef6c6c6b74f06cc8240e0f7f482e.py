#Contestador de celular
def contestar_celular(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"
        
    if hora < 14 and numero % 100 == 909:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"
        
    if hora >= 17 and hora < 19 and numero // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

resultado = contestar_celular(numero_telefonico, hora_llamada)
print("Resultado:", resultado)
