def jerigonzo (texto):
    traducida=""
    for letra in texto:
        traducida+=letra
        if letra.lower() in "aeiou":
             traducida+="p" + letra
    return traducida