def buscarTodas(a,b):
    p=0
    f=""
    while p>=0:
        p=a.find(b)
        x=str(p)
        p=int(p)
        a=a.replace(b,"1",1)
        if p>=0:
            f=f+" "+x
            f=f.strip(",")
            f=f.strip(" ")
    return f

    pass
if __name__ == "__main__":
    pass
           