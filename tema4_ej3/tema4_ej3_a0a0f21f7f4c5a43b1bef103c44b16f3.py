def jerigonzo(palabra):
    Vocales = ["a","e","i","o","u"]
    palabra_nueva =""
    for i in palabra:
        if i in Vocales:
            palabra_nueva += i+"p"+i
        else:
            palabra_nueva += i
    return palabra_nueva
