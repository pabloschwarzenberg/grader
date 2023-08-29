# completa el código de la función

def amigos(a,b):
    sumar=0
    sumare=0
    for i in range(1,a):
     if (a%i)==0:
      sumar=sumar+i
    for i in range(1,b):
     if (b%i)==0:
      sumare=sumare+i
    if sumar==b and sumare==a:
       return True 
    else:
       return False
 
           