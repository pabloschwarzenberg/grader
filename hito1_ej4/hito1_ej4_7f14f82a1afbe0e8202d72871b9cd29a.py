#Conversión de Decimal a Binario
def DecBinario(n):
    float(input("agregue un numero decimal"))
    d=[]
    print("el numero",n,end="  ")
    while(n>=1):
        d.append(n%2)
        n=int(n/2)

    s=d[ : :-1]
    print("corresponde al binario ",end=" ")
    for x in s:
        print(x,end=" ")
DecBinario()
