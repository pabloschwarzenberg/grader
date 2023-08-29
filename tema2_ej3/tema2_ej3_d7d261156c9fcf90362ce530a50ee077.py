def numero_perfecto(a):
    cuenta=0
    for n in range(1,a):
      if a%n==0:
        cuenta+=n
      else:
        pass
    if cuenta==a:
      return True
    else:
      return False
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           