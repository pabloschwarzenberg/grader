# completa el código de la función
def suma_divisores(n):
   divisor=1
   b=0
   while divisor<n:
     if n%divisor==0:
        b=b+divisor
     divisor=divisor+1
   return b, es_primo(b)
        
def es_primo(b):
    if b==1:
       return True
    else:
        return False
        
if __name__ == "__main__": 
   n=int(input())
   print (suma_divisores,",", es_primo)