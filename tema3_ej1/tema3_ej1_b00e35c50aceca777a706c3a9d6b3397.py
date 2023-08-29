def sumaDivisores(n):
   
    if n==1:
      return 1
    # Cualquier otro caso, hay que recorrer todos los números entre 2 y n
    # (ambos inclusive) buscando divisores
    for i in range(2,n+1):
      if n%i == 0: # Tenemos un divisor
        # Aplicamos recursividad
        return n + sumaDivisores(n//i)
    print 
    return (" su numero es primo")