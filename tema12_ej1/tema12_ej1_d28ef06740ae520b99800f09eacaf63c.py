#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
def binarios(n):
    
    for i in range(2**n):
        x = bin(i)[2:]
        x = "0" * (n-len(x)) + x
        print (x)
    return ""
        
print (binarios(n))

           