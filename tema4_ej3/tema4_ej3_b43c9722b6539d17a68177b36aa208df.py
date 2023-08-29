def jerigonzo(palabra):
    vocal=["a","e","i","o","u"]
    nueva_palabra=""
    for letra in palabra:
        if letra in vocal:
            nueva_palabra+=letra+"p"+letra
        else:
            nueva_palabra+=letra
    return (nueva_palabra)