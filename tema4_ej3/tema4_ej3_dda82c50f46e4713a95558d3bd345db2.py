def jerigonzo(string):
    vocales = ["a", "e", "i", "o", "u"]
    cant_vocales = 0
    traducida = ""
    for i in vocales:
        if i in string:
            if cant_vocales < 1:
                cant_vocales += 1
                print(cant_vocales)
                traducida = string.replace(i, i+"p"+i, 300)
            else:
                traducida = traducida.replace(i, i+"p"+i, 300)
    return traducida
if __name__ == "__main__":
    pass
         