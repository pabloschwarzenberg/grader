def suma_divisores(n):
    # Caso base que se resuelve directamente
    if n==1:
      return 0,False
    # Cualquier otro caso, hay que recorrer todos los números entre 2 y n
    # (ambos inclusive) buscando divisores
    for i in range(2,n+1):
      if n%i == 0: # Tenemos un divisor
        # Aplicamos recursividad
        return  n + suma_divisores(n//i)
       
