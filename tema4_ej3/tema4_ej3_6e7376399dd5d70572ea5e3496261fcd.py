def jerigonzo(palabra):
    vocal=""
    for letra in palabra:
        if letra in "AEIOUaeiou":
            vocal+=letra
            vocal+="p"
        vocal+=letra
    return vocal