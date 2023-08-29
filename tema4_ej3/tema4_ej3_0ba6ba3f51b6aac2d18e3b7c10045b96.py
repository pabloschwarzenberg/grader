def jerigonzo(string):
    string=list(string)
    for k in string[:]:
        if k=="a" or k=="e" or k=="i" or k=="o" or k=="u":
            posicion=string.index(k)
            string.insert(posicion+1,"p")
            string.insert(posicion+2,k)
    string="".join(string)
    return string

if __name__ == "__main__":
    pass
         