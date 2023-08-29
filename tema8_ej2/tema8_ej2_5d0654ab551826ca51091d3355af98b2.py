def buscarTodas(a,b):
    pos=""
    i=0
    while i < len(a):
        if a[i]==b:
            pos=pos+str(i)+" "
        i+=1
    return pos[:-1]

if __name__ == "__main__":
    pass
           