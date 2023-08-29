def jerigonzo(string):
    a=list(string)
    long=len(string)
    i=0
    while i<long:
        long=len(a)
        if a[i]=="a":
            a.insert(i+1,"pa")
        elif a[i]=="e":
            a.insert(i+1,"pe")
        elif a[i]=="i":
            a.insert(i+1,"pi")
        elif a[i]=="o":
            a.insert(i+1,"po")
        elif a[i]=="u":
            a.insert(i+1,"pu")
        i=i+1
    a="".join(a)
    return a

if __name__ == "__main__":
    palabra=input("Escriba la palabra que desea traducir: ")
    jerigonzo(palabra)
    pass
