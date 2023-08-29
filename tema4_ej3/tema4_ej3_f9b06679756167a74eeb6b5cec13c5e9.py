def jerigonzo(texto):
    jeri=""
    vocales=["a","e","i","o","u"]
    for letra in texto:
        if letra == ("a") or letra == ("e") or letra == ("i") or letra == ("o") or letra == "u":
            jeri+=letra+"p"+letra
                
        else:
            jeri+=letra
    return jeri
print(jerigonzo("estamos programando"))


         