def numero_perfecto(a):
 def sumadiv(a):
     s=0
     for i in range(1,a):
         if a%i==0:
            s=s+i
     return s
 
 if sumadiv(a)==a: 
    return True
 else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           