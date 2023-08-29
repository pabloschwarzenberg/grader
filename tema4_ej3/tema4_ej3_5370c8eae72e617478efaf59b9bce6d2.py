def jerigonzo(org):
    traduccion=""
    for letra in org:
        traduccion+=letra
        if letra.lower() in "aeiou":
            traduccion+="p"+letra
    return traduccion
         