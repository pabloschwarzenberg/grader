def decodificar(mensaje):
    mensaje2 = mensaje.strip().split(",")
    resultado = []
    i = 0
    while i < len(mensaje2):
        a = mensaje2[i]
        primero = int(a[0]) * (2 ** 7)
        segundo = int(a[1]) * (2 ** 6)
        tercero = int(a[2]) * (2 ** 5)
        cuarto = int(a[3]) * (2 ** 4)
        quinto = int(a[4]) * 8
        sexto = int(a[5]) * 4
        septimo = int(a[6]) * 2
        octavo = int(a[7]) * 1
        suma = primero + segundo + tercero + cuarto + quinto + sexto + septimo + octavo
        letra = chr(suma)
        resultado.append(letra)
        i += 1
    return "".join(resultado)