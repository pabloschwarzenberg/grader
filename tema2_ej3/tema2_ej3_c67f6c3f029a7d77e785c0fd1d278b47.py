def numero_perfecto(a):
    d=1
    s=0
    while d<a:
      if a%d==0:
        s=s+d
      d=d+1
    if s==a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    d=1
    s=0
    print(numero_perfecto(a))
           