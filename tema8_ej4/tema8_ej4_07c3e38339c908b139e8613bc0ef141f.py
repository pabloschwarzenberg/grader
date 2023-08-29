def rot13(palabra):
    parteSuperior = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    parteInferior = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    nuevomensaje = []

    for letra in palabra:
        contador = 0
        while contador < 13:
            if letra == parteSuperior[contador]:
                nuevaletra = parteInferior[contador]
                nuevomensaje.append(nuevaletra)
            elif letra == parteInferior[contador]:
                nuevaletra = parteSuperior[contador]
                nuevomensaje.append(nuevaletra)
            contador += 1

    codificado = "".join(nuevomensaje)

    return codificado
           