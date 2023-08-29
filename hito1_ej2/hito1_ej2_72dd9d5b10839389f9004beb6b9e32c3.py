def contestar_celular(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada <= 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and numero_telefonico % 100 == 909:
        return "CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

if __name__ == "__main__":
    numero_telefonico = int(input("Ingrese número telefónico: "))
    hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

    resultado = contestar_celular(numero_telefonico, hora_llamada)
    print("Resultado:", resultado)



     