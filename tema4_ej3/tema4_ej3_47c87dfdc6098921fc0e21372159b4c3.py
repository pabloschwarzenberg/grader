def jerigonzo(string):
    c=len(string)
    lista=[]
    Jerigonzo=""
    for d in range (c):
        ele=string[d]
        if ele=="a" or ele=="e" or ele=="i" or ele=="o" or ele=="u":
            ele=ele+"p"+ele
        lista.append(ele)
    for o in range(c):
        Jerigonzo=Jerigonzo+lista[o]
    string=Jerigonzo
    return string

if __name__ == "__main__":
    pass