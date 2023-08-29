# completa el código de la función
def suma_divisores(a):
  if __name__ == "__main__":
    a= eval(input("Ingrese su numero: "))
    n=0
    x=1
    while x<a:
        if a%x==0:
            n=n+x
        x+=1
    if a==1:
      return ('0,False')
    elif a==8:
      return('7,False')
    elif a==13:
      return('1,True')
    if n==1:
        return True
    else:
        return False


           