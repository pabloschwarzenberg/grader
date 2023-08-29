def jerigonzo(string):
    string=string.lower()
    vocales="aeiou"
    stringl=list(string)
    i=0
    while i < len(string):
        if vocales.find(stringl[i]) != -1:
            stringl[i]=stringl[i]+"p"+stringl[i]
        i=i+1
    string="".join(stringl)
    return string

if __name__ == "__main__":
    pass
         