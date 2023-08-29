# por favor escribe aquí tu función
def es_primo(num):
    i=2
    a=0
    if num==1:
      return False
    while i<num:
       if num%i==0:
           a=1
           return False
           break
       i=i+1
    if a!=1:
           return True