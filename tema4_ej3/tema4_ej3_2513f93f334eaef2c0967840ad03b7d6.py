def jerigonzo(string):
    string = string.lower()
    nuevo_string = ""
    for i in range(len(string)):
        nuevo_string += string[i]
        if string[i] in "aeiou":
            nuevo_string += "p" + string[i]
    return nuevo_string

if __name__ == "__main__":
    pass