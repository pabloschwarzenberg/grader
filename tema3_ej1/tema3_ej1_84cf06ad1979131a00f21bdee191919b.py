def suma_divisores(n):
    divisores = float(input("Ingrese el valor correspondiente"))

    for i in range(2,n + 1):
        if n % i == 0:
            divisores.append(i)

    def primos(n):
    losprimos=[]
    for x in range(2,n): #va del numero 2 al elejido
        val=True
        for y in range(2,x): #va del numero 2 al x
            if x%y == 0: #si el modulo de x e y es 0, no cumple la regla de los numeros primos
                val=False
                break
        if val: #si val es Flase no lo agrega, si es True lo hace
            losprimos.append(x)    
    return losprimos  
    