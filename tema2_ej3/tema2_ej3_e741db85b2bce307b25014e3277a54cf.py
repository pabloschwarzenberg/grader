def numero_perfecto(a):
    divisor=1
    t=0
    while divisor<a:
      if a%divisor==0:
         t=t+divisor
      divisor=divisor+1
    if t==a:
          return True
    else:
          return False
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           