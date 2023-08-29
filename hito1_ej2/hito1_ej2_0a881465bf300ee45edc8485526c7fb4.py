def contestar_celular(numero, hora):
    if 0 <= hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 9:
        return "CONTESTAR"
    elif 17 <= hora <= 19 and numero // 1000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

resultado = contestar_celular(numero, hora)
print("Resultado:", resultado)