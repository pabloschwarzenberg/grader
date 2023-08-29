letras = ["A", "a", "C", "c", "T", "t", "G", "g"]


def carlos(c):
    for b in c:
        if b not in letras:
            return "incorrecta"
    return "correcta"


a = input()
print(carlos(a))