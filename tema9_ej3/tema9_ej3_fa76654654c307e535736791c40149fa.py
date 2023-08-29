def decodificar(palabra):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alfabetobin = ["01100001","01100010","01100011","01100100","01100101","01100110","01100111","01101000","01101001","01101010","01101011","01101100","01101101","01101110","01101111","01110000","01110001","01110010","01110011","01110100","01110101","01110110","01110111","01111000","01111001","01111010","01111011","01111100","01111101","01111110"]
    lista_palabra = palabra.split(",")
    palabra_decodificada = []
    for i in range(0, len(lista_palabra)):
        for j in range(0, len(alfabeto)):
            if lista_palabra[i] == alfabetobin[j]:
                letra_cambiada = alfabeto[j]
                palabra_decodificada.append(letra_cambiada)
    return "".join(palabra_decodificada)