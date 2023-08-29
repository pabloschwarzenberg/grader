# completa el código de la función
def suma_divisores(a):
    i=1
    s=0

    while i<a:
        if a%i==0:
            s+=i
        i+=1

    if s!=1:
      return s,False
    else:
      return s,True
        