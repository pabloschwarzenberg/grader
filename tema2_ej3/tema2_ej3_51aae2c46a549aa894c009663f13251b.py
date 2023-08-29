# Números Perfectos
def numero_perfecto(x):
    suma, n = 0, 1
    
    while n < x:
        if x % n == 0:
            suma = suma + n
        
        n += 1
    
    if suma == x:
        return True
    else:
        return False

if __name__ == "__main__":
    num =int(input("Ingrese un número natural: "))
    
    print(numero_perfecto(num))