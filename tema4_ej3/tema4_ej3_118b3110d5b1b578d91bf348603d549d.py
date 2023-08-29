def jerigonzo(string):
    vocales = ["a","e","i","o","u"]
    string = list(string)
    k = 0
    for i in string:
        if i in vocales:
            string[k] = i+"p"+i
            k += 1
        else:
            k += 1
            continue
        z = ""
    for u in string:
        z += u
    string = z
    return string

if __name__ == "__main__":
    palabra = str(input())
    traduccion = jerigonzo(palabra)
    print(traduccion)

         