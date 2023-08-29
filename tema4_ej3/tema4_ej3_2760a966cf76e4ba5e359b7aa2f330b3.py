def jerigonzo(string):
    palabra = ""
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            palabra += i + "p" + i
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            palabra += i
    return palabra
if __name__ == "__main__":
    pass 