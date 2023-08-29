def numero_perfecto(a):
    x=0
    divisor=a-1
    
    while divisor>=1:
      if a%divisor==0:
        x+=divisor
      divisor-=1
    if x==a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           