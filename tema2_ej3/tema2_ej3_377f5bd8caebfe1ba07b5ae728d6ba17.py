def numero_perfecto(a):
    division=1
    guardo=0
    while division!=a:
      if(a%division==0):
        guardo=guardo+division
        division=division+1
      else:
         division=division+1
    if guardo==a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           