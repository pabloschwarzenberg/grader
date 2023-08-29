def numero_perfecto(a):
    n1=0
    for i in range (1,a):
      if a%i==0:
        n1=n1+i
    if n1==a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
