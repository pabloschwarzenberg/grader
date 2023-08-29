def rot13(palabra):
    palabra = str(palabra)
    letrasMay = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM"
    letrasMin = "abcdefghijklmnopqrstuvwxyzabcdefghijklm"
    p_codificada = ""
    for i in range(len(palabra)):
        if palabra[i] in letrasMay:
            ubicacion = letrasMay.find(palabra[i])
            p_codificada += letrasMay[ubicacion + 13]
        elif palabra[i] in letrasMin:
            ubicacion = letrasMin.find(palabra[i])
            p_codificada += letrasMin[ubicacion + 13]
    return p_codificada