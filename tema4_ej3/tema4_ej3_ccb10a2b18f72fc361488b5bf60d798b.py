def jerigonzo(texto):
    jer=""
    vocales=["a","e","i","o","u"]
    for letra in texto:
        if letra== ("a") or letra == ("e") or letra == ("i") or letra == ("o") or letra =="u":
            jer+=letra+"p"+letra
        else:
            jer+=letra
    return jer
print(jerigonzo("estamos programados"))
