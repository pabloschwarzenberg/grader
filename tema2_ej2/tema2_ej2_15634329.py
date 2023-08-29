# completa el código de la función
def amigos(a,b):
    s=0;S=0
    for i in range(1,a):
      if a%i==0:
          s+=i
    for i in range(1,b+1):
      if b%i==0:
          S+=i 
    return s==b or S==a
           