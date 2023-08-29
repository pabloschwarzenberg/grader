def jerigonzo(string):
    string = list(string)
    string2 = list(string)
    c = 0
    for i in range(len(string)):
        if string2[i] == "a":
            string.insert(i+1+c,"p")
            string.insert(i+2+c,"a")
            c = c+2
        elif string2[i] == "e":
            string.insert(i+1+c,"p")
            string.insert(i+2+c,"e")
            c = c+2
        elif string2[i] == "i":
            string.insert(i+1+c,"p")
            string.insert(i+2+c,"i")
            c = c+2
        elif string2[i] == "o":
            string.insert(i+1+c,"p")
            string.insert(i+2+c,"o")
            c = c+2
        elif string2[i] == "u":
            string.insert(i+1+c,"p")
            string.insert(i+2+c,"u")
            c = c+2
    string = "".join(string)
    return string

if __name__ == "__main__":
    string = input("texto: ")
    print(jerigonzo(string))
    pass
