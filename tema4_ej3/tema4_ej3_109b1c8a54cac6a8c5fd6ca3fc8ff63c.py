def jerigonzo(x):
    x=list(x)
    largo=len(x)
    a=0
    while a < largo:
        if x[a]=="a":
            x.insert(a+1,"pa")
        if x[a]=="e":
            x.insert(a+1,"pe")
        if x[a]=="i":
            x.insert(a+1,"pi")
        if x[a]=="o":
            x.insert(a+1,"po")
        if x[a]=="u":
            x.insert(a+1,"pu")
        a+=1
        largo=len(x)
    x="".join(x)
    return x


if __name__ == "__main__":
    pass
         