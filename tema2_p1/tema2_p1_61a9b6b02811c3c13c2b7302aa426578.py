# por favor escribe aquí tu función
def es_primo(n):
   divisores = [1]
    
   for i in range(2, n +1):
      if n % i == 0:
         divisores.append(i)
        
   return (sum(divisores) - n)


resultado = es_primo(7)

print (resultado)

if (resultado == 1):
   print("True")  #Es primo
else:
   print("Flase") #No lo es
