def jerigonzo(string):
    lst= list(string)
    vocales= list("aeiou")
    for j in range (0,len(string)):
        for i in range(0,len(vocales)):
            if lst[j] == vocales[i]:
                lst[j]=vocales[i]+"p"+vocales[i]
        string="".join(lst)
    return string
    
if __name__ == "__main__":
    pass
         