def jerigonzo(string):
    convertido = []
    for p in string:
        for l in p:
            if l in "aeiouAEIOU":
                l = l + "p"+ l
            convertido.append(l)
    convertido = "".join(convertido)
    return convertido