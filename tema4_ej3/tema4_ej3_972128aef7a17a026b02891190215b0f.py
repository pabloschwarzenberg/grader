def jerigonzo(string):
    traducido = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra 
            traducido.append(letra)
    traducido = "".join(traducido)
    return traducido
           
         