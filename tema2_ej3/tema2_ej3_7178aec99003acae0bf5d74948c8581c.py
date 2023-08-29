def numero_perfecto(a):
    t=0
    if a==1:
      return False
    else:
      for i in range(1,a):
        if(a%i==0):
          t=t+i
      if t==a:
        return True
      else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           