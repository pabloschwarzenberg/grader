#Contestador de celular
#Ingreso de datos
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese la hora de la llamada: "))

#parametros para ver si contestar o no
def contestar(numero, hora):
    if hora >= 0 and hora<7:
        return "Contestar"
    if hora < 14 and numero %100 != 909:
        return "Contestar"
    if hora >= 17 and hora <19 and numero //10000000 == 877:
        return "Contestar"
    else:
        return"No contestar"
        
#Imprimir resultado
siono = contestar(numero, hora)
print("Resultado", siono)