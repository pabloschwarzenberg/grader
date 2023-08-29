a=input("Ingrese String:")
n=int(input("Ingrese numero:"))
solo_n=[]
unica=[]
if(len(a)>=n):
    for i in range(len(a)-n+1):
        solo_n.append(a[i:n+i])
        unica.append(0)

    a=0
    b=0

    while(a<(len(solo_n))):
        b=b+1
        c=b
        while(c<len(solo_n)):
            if( solo_n[a] == solo_n[c] ):
                unica[a]=1
                unica[c]=1
            c=c+1
        a=a+1
    
    total=len(unica)
    total_1=0
    
    resultado=[]
    
    for i in unica:
        total_1=total_1+i

    if(total==total_1):
        resultado.append("ninguna")
    else:
        for i in range(len(unica)):
            if(unica[i]==0):
                resultado.append(solo_n[i])
    print(resultado)