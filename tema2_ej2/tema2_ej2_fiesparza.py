# completa el código de la función
def suma_divisores(x):
   suma=0
   valor=1
   while valor< x:
       if x%valor==0:
         suma+=valor
       valor +=1
   return suma

def amigos(x,y):
    if x==y:
       return False 
    if suma_divisores(x)==y and suma_divisores(y)==x:
       return True
   
  
    return False
           