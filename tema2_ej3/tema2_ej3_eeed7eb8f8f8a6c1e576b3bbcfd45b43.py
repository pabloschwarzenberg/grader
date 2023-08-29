def numero_perfecto(a):
    
    var_sumatoria = 0
    
    for p in range(1, a):
        if a % p == 0:
            var_sumatoria += p
            
    if a == var_sumatoria:
        return True
    else:
        return False
    
if __name__ == "__main__":
    a = int(input("Ingrese el número a evaluar: "))
    print(numero_perfecto(a))