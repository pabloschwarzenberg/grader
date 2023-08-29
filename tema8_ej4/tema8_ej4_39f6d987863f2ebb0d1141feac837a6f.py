def rot13(palabra):
    abecedario= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    rot13=      ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    lista_palabra= []
    cifrado= []
    for letra in palabra:
        lista_palabra.append(letra)
    for letra in lista_palabra:
        pos=0
        while pos< len(abecedario):
            if letra== abecedario[pos]:
                cifrado.append(rot13[pos])
            pos= pos + 1
    pala= ""
    for letra in cifrado:
        pala= pala + letra
    return(pala)
           