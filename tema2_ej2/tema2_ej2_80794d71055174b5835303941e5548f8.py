# completa el código de la función
a=int(input("ingrese un numero:"))
b=int(input("ingrese un  numero:"))
def divisor (x):
  
    suma = int(0)
    for k in  range(1, int(x / 2) + 1):
    
        if((x % k) ==0):
              suma = suma +k
    
    return suma
    
    
for i in range(a,b):
    ri = int(divisor(i))
    
    for j in range(i,b):
    
          rj = int(divisor(j))
          
          if((ri == j) and (rj == i)):
          
               print( str(i) + " /t" + str(j) + "/t son numeros amigos")
           