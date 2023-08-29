def buscarTodas(a,b):
    a=list(a)
    y=[]
    azul=len(a)-1
    for i in range(0,len(a)):
        if a[i]==b:
            y.append(str(i))
            y.append(' ')
    y=y[:len(y)-1]        
    y=''.join(y)
    return str(y)
    pass

if __name__ == "__main__":
    a=input('a: ')
    b=input('b: ')
    print(buscarTodas(a,b))

    pass