def buscarTodas(a,b):
    palabra=[]
    for k in a:
        if k==b:
            c=a.index(k)
            print(c)
            palabra.append(c)
            a=a.replace(b," ",1)
            print(a)
    p=str(palabra).replace("[","").replace("]","").replace(", "," ")
    print(p)
    return p

if __name__ == "__main__":
    a=input()
    b=input()
    print(buscarTodas(a,b)) 