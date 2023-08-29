def jerigonzo(string):
    jerigonzo1 = list(string)
    i = 0
    while i < len(jerigonzo1) :
        if jerigonzo1[i] == "a" or jerigonzo1[i] == "e" or jerigonzo1[i] == "i" or jerigonzo1[i] == "o" or jerigonzo1[
            i] == "u":
            jerigonzo1.insert(i + 1, "p")
            jerigonzo1.insert(i + 2, jerigonzo1[i])
            i += 3
        else:
            i += 1
    jerigonzo1 = "".join(jerigonzo1)
    return jerigonzo1

print(jerigonzo("hola"))
         