def suma_divisores(a):
    divisores = [1]
    x = 0
    for i in range(2, a + 1):
        if a % i ==0:
            divisores.append(i)
        
    for i in range(1,a+1):
        if(a % i==0):
            x=x+1
        if(x!=2):
            print(a,"No es primo")
            break
        else:
            print(a, "si es primo")
    return sum(divisores)

if __name__ == "__main__":
    a = 12
    resultado = suma_divisores(a) - a
    print("La suma de sus divisores es", resultado)