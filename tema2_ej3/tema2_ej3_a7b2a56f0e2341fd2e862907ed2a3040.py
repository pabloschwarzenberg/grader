def numero_perfecto(a):
   s=0
   for d in range (1,a):
        if a==1:
           s=0
        elif a%d==0:
            s=s+d
   if s==a:        
      return True
   else:
      return False 

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           