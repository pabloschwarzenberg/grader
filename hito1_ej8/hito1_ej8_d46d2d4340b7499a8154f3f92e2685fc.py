#Descomponer un número
if __name__ == '__main__':
    
    print("Ingrese Número de 4 Cifras : ")  
    n = int(input())
    M = int((n - (n % 1000)) / 1000)
    C = int((n % 1000) / 100)
    D = int((n % 100) / 10)
    U = n % 10
    print (M,'M',(C),'C',(D),'D',(U),'U')
    