def mcm(a,b,ab):
    if a<b:
      if b%a == 0:
          return (ab)/a
          
      else:
          aux = b%a
          return mcm(a,aux,ab)

    if b<a:
      if a%b == 0:
          return (ab)/b
      
      else:
          aux = a%b
          return mcm(aux,b,ab)
   
    
          

if __name__=="__main__":
    a = int(input("Ingrese su a: "))
    b = int(input("Ingrese su b: "))
    ab = a*b
           
    print(mcm(a,b,ab))
           