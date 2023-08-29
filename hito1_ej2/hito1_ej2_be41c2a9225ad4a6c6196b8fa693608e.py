#Contestador de celular
def contestar_llamada(num_telefonico, h_llamada):
    if h_llamada >= 0 and h_llamada < 7:
        return "CONTESTAR"
    elif h_llamada < 14 and num_telefonico % 1000 == 909:
        return "CONTESTAR"
    elif h_llamada >= 17 and h_llamada < 19 and num_telefonico // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

num_telefonico = int(input("Ingrese numero telefonico: "))
h_llamada = int(input("Ingrese hora de la llamada: "))

resultado = contestar_llamada(num_telefonico, h_llamada)
print("Resultado:", resultado)
