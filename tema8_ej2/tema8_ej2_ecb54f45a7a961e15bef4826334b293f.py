def buscarTodas(a,b):
    c=list(a)
    d=len(c)
    l=[]
    for i in range(0,d):
        if b==c[i]:
            l.append(str(i))
    return (" ".join(l))

#x=input()
#y=input()
#print(buscarTodas(x,y))

if __name__ == "__main__":
    pass
           