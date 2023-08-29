def rot13(palabra):
    palabra_codificada=""
    abcdario = "abcdefghijklmnopqrstuvwxyzabcdefghijklm"
    lista_abcdario = list(abcdario)
    
    for letra in palabra:
        i=0
        while True:
            if letra == lista_abcdario[i]:
                palabra_codificada += lista_abcdario[i+13]
                break
            i += 1
    return palabra_codificada