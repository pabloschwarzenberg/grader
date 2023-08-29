def jerigonzo(palabra):
    palabra=palabra.lower()
    palabra=palabra.replace("a","apa",len(palabra))
    palabra=palabra.replace("e","epe",len(palabra))
    palabra=palabra.replace("i","ipi",len(palabra))
    palabra=palabra.replace("o","opo",len(palabra))
    palabra=palabra.replace("u","upu",len(palabra))
    return palabra

