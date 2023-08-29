def jerigonzo(string):
    i=0
    sto=string.lower()
    stro=list(sto)
    while i<len(stro):
        if stro[i] == "a" or stro[i] == "e" or stro[i] == "i" or stro[i] == "o" or stro[i] == "u":
            stro[i]=stro[i]+"p"+stro[i]
            i=i+1
        elif stro[i]!="a" and stro[i]!="e" and stro[i]!="i" and stro[i]!="o" and stro[i]!="u":
            stro[i]=stro[i]
            i=i+1
    if i==len(string):
        string="".join(stro)
        return string


if __name__ == "__main__":
    pass
         