#Contestador de celular
def contestar_llamada(hora, numero):
    if 0 <= hora <= 7:
        return "CONTESTAR"
    if hora < 14 and (numero % 100 == 909 or numero < 0 or numero > 14):
        return "CONTESTAR"
    if 17 <= hora <= 19 and numero // 1000000 == 877:
        return "CONTESTAR"
    return "NO CONTESTAR"
numero = int(input("Ingresa el número de celular que llama: "))
hora = int(input("Ingresa la hora: "))
resultado = contestar_llamada(hora, numero)
print(resultado)