def rot13(palabra):
    palabra_final = ""
    c1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    c2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    i = 0
    while i < len(palabra):
        indice = palabra[i]
        if indice in c1:
            for k in range(13):
                if indice == c1[k]:
                    palabra_final += c2[k]
        elif indice in c2:
            for w in range(13):
                if indice == c2[w]:
                    palabra_final += c1[w]
        i += 1
    return palabra_final
   
