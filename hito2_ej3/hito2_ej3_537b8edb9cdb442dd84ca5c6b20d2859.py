def revisar(f,g):
    i = 1
    l = []
    x = len(f) - g
    subcadena = ""
    k=0
    if f[1]==f[2] and f[3]==f[2] and f[4]==f[3]:
        k=6000
    while x>i:
        for q in range(i,i+g):
           subcadena=subcadena+f[q]
        l.append(subcadena)
        subcadena=""
        i=i+1

    
    b=0
    while len(l)>k:
        a=l[k]
        p=f.count(a)
        if p==1:
            print(a)
            k=k+1
            b=b+1
        else:
            b=b
            k=k+1
    if b==0:
        print("ninguna")
    

secuencia=input("secuencia: ")
n=int(input("numero: "))
revisar(secuencia,n)      