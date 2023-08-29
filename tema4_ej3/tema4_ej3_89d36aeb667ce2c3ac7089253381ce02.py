def jerigonzo(string):
    convertido = []
    for pal in string:
        for l in pal:
            if l in "aeiouAEIOU":
                l = l + "p"+ l
            convertido.append(l)
    convertido = "".join(convertido)
    return convertido
         