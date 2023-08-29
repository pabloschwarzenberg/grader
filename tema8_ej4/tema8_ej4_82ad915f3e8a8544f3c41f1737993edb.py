def rot13(txt):
    cifrado = ""
    Desplazamiento = 13
    Letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(txt)):
        for j in range(len(Letras)):
            if txt[i] == Letras[j]:
                if j + Desplazamiento > 25:
                    diff = (j + Desplazamiento) - 25
                    cifrado = cifrado + (Letras[diff -1])
                else:
                    cifrado = cifrado + (Letras[j+Desplazamiento])
    return cifrado