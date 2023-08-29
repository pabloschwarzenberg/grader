def jerigonzo(string):
    elflint = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            elflint.append(letra)
    elflint = "".join(elflint)
    return elflint
         