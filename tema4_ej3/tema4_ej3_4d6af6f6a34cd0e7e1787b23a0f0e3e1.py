def jerigonzo(string):
    string=str(string)
    vocales="aeiou"
    for i in vocales:
        string=string.replace(i,i+"p"+i)
    return (string)


if __name__ == "__main__":
    pass
         