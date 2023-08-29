def jerigonzo(palabra):
    v=list(palabra)
    i=0
    while i<=len(v)-2:
        if v[i]=="a":
            v.insert(i+1,"p")
            v.insert(i+2,"a")
            i=i+3
        elif v[i]=="e":
            v.insert(i+1,"p")
            v.insert(i+2,"e")
            i=i+3
        elif v[i]=="i":
            v.insert(i+1,"p")
            v.insert(i+2,"i")
            i=i+3
        elif v[i]=="o":
            v.insert(i+1,"p")
            v.insert(i+2,"o")
            i=i+3
        elif v[i]=="u":
            v.insert(i+1,"p")
            v.insert(i+2,"u")
            i=i+3
        else:
            i=i+1
    if v[len(v)-1]=="a":
        v.insert(len(v),"p")
        v.insert(len(v)+1,"a")
    elif v[len(v)-1]=="e":
        v.insert(len(v),"p")
        v.insert(len(v)+1,"e")
    elif v[len(v)-1]=="i":
        v.insert(len(v),"p")
        v.insert(len(v)+1,"i")
    elif v[len(v)-1]=="o":
        v.insert(len(v),"p")
        v.insert(len(v)+1,"o")
    elif v[len(v)-1]=="u":
        v.insert(len(v),"p")
        v.insert(len(v)+1,"u")
        
    palabra="".join(v)
    return palabra 

if __name__ == "__main__":
    pass
    a=input()
    print(jerigonzo(a))