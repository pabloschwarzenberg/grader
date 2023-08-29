def numero_perfecto(x):
    suma=0
    valor=1
    while valor< x:
       if x%valor==0:
         suma+=valor
       valor +=1
    
    if suma==x:
       return True
    else:
    
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           