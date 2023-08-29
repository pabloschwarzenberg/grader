def jerigonzo(originales):
    cifradas = []
    for palabra in originales:
        palabra_nueva = ""
        for letra in palabra:
            nueva_letra=letra
            if letra == "a"or letra=="e"or letra=="i" or letra=="o" or letra=="u":
                nueva_letra = letra+"p"+letra
            palabra_nueva = palabra_nueva + letra
            cifradas.append(nueva_letra)
    return ''.join(str(i) for i in cifradas)

if __name__ == "__main__":
    pass
         