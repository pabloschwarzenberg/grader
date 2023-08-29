# completa el código de la función
n = input('ingrese su primer numero: ')
m = input('ingrese su segundo numero: ') 
suma = 0    
   
for i in range(1,n): 
        if n % i == 0: 
            suma += i
            if (amigos(n)==m and amigos(m)==n):
             return True
             else:
             return False
