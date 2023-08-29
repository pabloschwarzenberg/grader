def jerigonzo(s):
    convertido = []
    for p in s:
        for l in p:
            if l in "aeiouAEIOU":
                l = l + "p"+ l
            convertido.append(l)
    convertido = "".join(convertido)
    return convertido
         