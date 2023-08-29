def rot13(string):
    palabra_final=""
    lista1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    lista2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    i = 0
    while i < len(string):
        indice = string[i]
        if indice in lista1:
            for k in range(13):
                if indice == lista1[k]:
                    palabra_final += lista2[k]
        elif indice in lista2:
            for w in range(13):
                if indice == lista2[w]:
                    palabra_final += lista1[w]
        i += 1
    return palabra_final
           