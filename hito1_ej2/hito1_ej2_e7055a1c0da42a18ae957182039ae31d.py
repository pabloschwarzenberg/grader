#Contestador de celular
def contestar_llamada(numero_telefonico, hora_llamada):#ojo con los espacios, python es sensible a los espacios en la sangria
    if hora_llamada >= 0 and hora_llamada <= 7:
        contestar_llamada="CONTESTAR"
        return contestar_llamada
    elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
        contestar_llamada="CONTESTAR"
        return contestar_llamada
    elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 10000000 == 877:
        contestar_llamada="CONTESTAR"
        return contestar_llamada
    else:
        contestar_llamada="NO CONTESTAR"
        return contestar_llamada  
        


numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

resultado = contestar_llamada(numero_telefonico, hora_llamada)
print("Resultado:", resultado)