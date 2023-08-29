n=int(input("-->"))
cont=2
while cont*cont<=n:
    while (n%cont)==0:
        print(cont)
        n//=cont
    cont=cont+1
if n>1:
    print(n)

