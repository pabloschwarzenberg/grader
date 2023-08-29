# agregar p despues de cada vocal
# repetir la vocal
def jerigonzo(original):
    traducida = ""
    for letra in original:
        traducida += letra
        if letra.lower() in "aeiou":
            traducida += "p" + letra
    return traducida

         