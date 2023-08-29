# completa el código de la función
def suma_divisores(a):
    i=1
    suma_divisores=0
    while i<a:
        if a%i==0:
            suma_divisores+=i
        i+=1
    return suma_divisores,(suma_divisores==1)
        
          
  
           