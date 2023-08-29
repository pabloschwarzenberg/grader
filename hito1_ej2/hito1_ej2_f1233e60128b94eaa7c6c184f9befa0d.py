def contestar_celular(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and not numero % 100 == 909:
        return "NO CONTESTAR"
    elif hora >= 17 and hora < 19 and not numero // 10000000 == 877:
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

if __name__ == "__main__":
    numero_telefonico = int(input("Ingrese numero telefonico: "))
    hora_llamada = int(input("Ingrese hora de la llamada: "))
    resultado = contestar_celular(numero_telefonico, hora_llamada)
    print("Resultado:", resultado)
