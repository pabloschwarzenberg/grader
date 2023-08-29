vocales = ["a", "e", "i", "o", "u"]
def jerigonzo(string):
    posicion = 0
    string = list(string)
    for i in string:
        i = i.lower()
        for j in vocales:
            if i == j:
                string[posicion] = i + "p" + i
        posicion += 1
    string = "".join(string)
    return string

if __name__ == "__main__":
    palabra = input()
    print(jerigonzo(palabra))