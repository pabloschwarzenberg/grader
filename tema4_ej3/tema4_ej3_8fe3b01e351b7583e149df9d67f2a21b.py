def jerigonzo(string):
    vocal = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    i = 0
    contador = 0
    string = list(string)
    while i < len(string):
        for n in vocal:
            if string[i] == n:
                string[i] = string[i] + "p" + string[i]
        i += 1
    string= "".join(string)

    return string
         