def DecBin(n):
    d=[]
    print("El numero", n,end=' ')
    while(n>=1):
        d.append(n%2);
        n=int(n/2);
        
    S = d[::-1]
    print("corresponde al binario: ",end=' ')
    for k in S:
        print (k, end=' ')
DecBin(33)
