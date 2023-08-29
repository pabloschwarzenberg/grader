#Conversión de Decimal a Binario

def DecaBin (n):
    

    a=[]
    
    print("El numero binario: ",n,end=' ')
    while (n>=1):
        a.append(n%2);
        n=int(n/2);
    b=a[::-1]    

    print(" de Binario a decimal es igual a: ", end='' )
    for k in b:
        print(k,end='')

DecaBin(int(input("Introduzca el decimal a converitr a binario: ")))