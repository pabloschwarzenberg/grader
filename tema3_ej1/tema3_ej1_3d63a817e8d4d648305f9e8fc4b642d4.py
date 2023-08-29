def suma_divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
        
    primo = sum(divisores)==1
    return sum(divisores), (primo)
    
if __name__=="__main__":
    n= int(input("ingrese numero: "))
    resultado = suma_divisores(n)
    print(resultado)