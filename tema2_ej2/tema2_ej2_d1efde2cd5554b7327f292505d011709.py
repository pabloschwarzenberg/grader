# completa el código de la función

def amigos(num): 
    suma = 0 
 
    for i in range(1,num): 
        if num % i == 0: 
            suma += i 
    return suma 
     
n = input('primer numero: ') 
m = input('segundo numero: ') 
 
for amigos(n) and amigos (m): 
  if amigos(n) == m and amigos(m) == n: 
    return True
  else:
    return False
  

           