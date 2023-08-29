#Conversión de Decimal a Binario
n = int(input("Ingrese un número: "))
def DecimalBinario(n):
    d = []
    while(n>=1):
        d.append(n%2);
        n = int(n/2);
        
    S = d[::-1]
    
    print("Resultado=" , end= "")
    for j in S:
        print(j, end="")
    
DecimalBinario(n)