def jerigonzo(string):
    string = list(string)
    string1 = string
    for i in range (0, len(string)):
        if string[i] == "a":
            string[i] = "apa"
        elif string[i] == "e":
            string[i] = "epe"
        elif string[i] == "i":
            string[i] = "ipi"
        elif string[i] == "o":
            string[i] = "opo"
        elif string[i] == "u":
            string[i] = "upu"
    string = "".join(string)
    return string


if __name__ == "__main__":
    string = input("metelo papu (la palabra)")
    a = jerigonzo(string)
    print (a)
