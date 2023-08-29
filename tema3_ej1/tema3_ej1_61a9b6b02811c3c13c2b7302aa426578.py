# completa el código de la función
def suma_divisores(n):
   divisores = [1]  
    
   for i in range(2, n +1):
      if n % i == 0:
         divisores.append(i)
        
   return (sum(divisores) - n)

resultado = suma_divisores(1)
resultado = suma_divisores(8)
resultado = suma_divisores(13)
if (resultado == 1):
  print("Es primo")
else:
  print("No es primo")



