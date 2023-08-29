def numero_perfecto(a):
    a=int(a)
    sumatoria=0
    for i in range (1,a):
        if a%i==0:
            sumatoria+=i
        elif a%i!=0:
            sumatoria+=0
         
    if sumatoria==a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           