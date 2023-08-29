def jerigonzo(string):
    palabra = list()
    p = -1
    vocal = ["a", "e", "i", "o", "u"]
    for i in range(len(string)):
        if string[i] in vocal:
            palabra.append(string[p + 1:i+1])
            p = i
            palabra.append("p")
            palabra.append(string[i])
            print(palabra)
    e = "".join(palabra)

    return e

if __name__ == "__main__":
    pass
         
#encontramos vocal
#cortamos y pegamos p + vocal 