def suma(n):
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    
    return sum(divisores)
resultado = suma(int(input("ingresar :")) 
print(resultado)