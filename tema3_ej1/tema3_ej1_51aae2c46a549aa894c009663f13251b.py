# Suma de los divisores de un número
def suma_divisores(x):
    if x == 1:
        suma, n_p = 0, False
    else:
        suma, n_p, n = 1, True, 2
        
        while n < x:
            if x % n == 0:
                suma = suma + n
            
            n += 1
        
        if suma > 1:
            n_p = False
    
    return suma, n_p

if __name__ == "__main__":
    num = int(input("Ingrese un número entero: "))
    
    suma_div, num_primo = suma_divisores(num)
    
    print("(" + str(suma_div) + ",", str(num_primo) + ")\n")