def jerigonzo(string):
    a=list(string)
    c=len(a)
    d=0
    while d<c:
        if a[d]=="a":
           a.insert(d+1,"p")
           a.insert(d+2,"a")
           c=c+2
           d=d+3
        elif a[d]=="e":
           a.insert(d+1,"p")
           a.insert(d+2,"e")
           c=c+2
           d=d+3
        elif a[d]=="i":
           a.insert(d+1,"p")
           a.insert(d+2,"i")
           c=c+2
           d=d+3
        elif a[d]=="o":
           a.insert(d+1,"p")
           a.insert(d+2,"o")
           c=c+2
           d=d+3
        elif a[d]=="u":
           a.insert(d+1,"p")
           a.insert(d+2,"u")
           c=c+2
           d=d+3
        else:
           d=d+1
    z="".join(a)
    return z
        

         