n = int(input("Ingrese digito n: "))
def suma_divisores(n):
   divisores = [1]
    
   for i in range(2, n +1):
      if n % i == 0:
         divisores.append(i)
        
   return (sum(divisores) - n)


resultado = suma_divisores(n)

if resultado == n:
    print("True")
else:
    print("False")
