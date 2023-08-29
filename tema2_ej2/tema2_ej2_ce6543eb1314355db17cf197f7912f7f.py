def sumadivisores(n):
    suma = 0
    for i in range(1,n//2 + 1,1):
        if n % i == 0: suma += i
    return suma
    
   for n in range(100000):
       if n % 1000 == 0: print(".",end=" ")
       otro = sumadivisores(n)
       if otro < n:
           if sumadivisores(otro) == n:
               print()
               print(n, otro)