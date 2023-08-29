def rot13(palabra):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    rot13="nopqrstuvwxyzabcdefghijklmn"
    txt = []
    for i in palabra:
        p=alfabeto.find(i)
        rot13=list(rot13)
        letra=rot13[p]
        txt.append(letra)
    respuesta="".join(txt)
    return respuesta