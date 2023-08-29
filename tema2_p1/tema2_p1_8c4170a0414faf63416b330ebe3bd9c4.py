#NUMEROS PRIMOS

#ENTRADA

def es_primo(x):

  if x > 1:

    p = 2

    a = 0
    
#PROCESAMIENTO

    while p < x:

      r = x % p

      if r == 0:

        a+=1

      p+=1

    if a == 0:

      return True

    else:

      return False

  else:

    return False
    
#SALIDA
  
try:

  x_in = eval(input("Inserta un valor entero: "))

  print(es_primo(x_in))
  
except:

  print("Inserte solamente un valor numerico")
  


