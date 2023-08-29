def jerigonzo(string):
    string=list(string)
    largo=len(string)
    a=0
    while a < largo:
        if string[a]=="a":
            string.insert(a+1,"pa")
        if string[a]=="e":
            string.insert(a+1,"pe")
        if string[a]=="i":
            string.insert(a+1,"pi")
        if string[a]=="o":
            string.insert(a+1,"po")
        if string[a]=="u":
            string.insert(a+1,"pu")
        a+=1
        largo=len(string)
    string="".join(string)
    return string
if __name__ == "__main__":
    pass
         