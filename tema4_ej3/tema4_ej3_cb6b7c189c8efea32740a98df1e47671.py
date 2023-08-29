def jerigonzo(string):
    L=""
    n=0
    while n<len(string):
        if string[n]=="a" or string[n]=="e" or string[n]=="i" or string[n]=="o" or string[n]=="u" :
            L=L+string[n]+"p"+string[n]
        else:
            L=L+string[n]
        n=n+1
    string=L
    return string

if __name__ == "__main__":
    pass
         