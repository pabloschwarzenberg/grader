# completa el código de la función
def amigos(n,m): 
    suma = 0 
 
    for i in range(1,m): 
        if m % i == 0: 
            suma += i 
    return suma 
if __name__ == "__main__":    
  n = input('primer numero: ') 
  m = input('segundo numero: ') 
 
  if amigos(n) == m and amigos(m) == n: 
      print ('los numeros %d y %d son amigos') %(n,m) 

    
    
           