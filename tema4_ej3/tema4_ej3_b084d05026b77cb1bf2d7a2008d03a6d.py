def jerigonzo(string):
    vocales = ["a", "e", "i", "o", "u"]
    string = list(string)
    for i in range(0, len(string)):
        for j in range(0, len(vocales)):
            if string[i] == vocales[j]:
                string[i]= string[i] + "p" + vocales[j]
                break
    string = "".join(string)
    return string


if __name__ == "__main__":
    pass
         