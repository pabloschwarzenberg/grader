# por favor escribe aquí tu función
def es_primo(n):
     if n==1:
         return False
     for i in range(2,n):
         if n%i ==0:
             return False
         elif n==1:
             return False
         elif n%i !=0:
             return True
             break