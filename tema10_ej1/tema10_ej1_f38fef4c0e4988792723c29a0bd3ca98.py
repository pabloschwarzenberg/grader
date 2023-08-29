def mcd(a,b,l,i):
    a=int(a)
    b=int(b)
    if a>b:
       if i<=b:
          if a%i==0 and b%i==0:
              l.append(i)
          i+=1
          return mcd(a,b,l,i)
       else:
            return l
    elif b>a:
         if i<=a:
            if a%i==0 and b%i==0:
                l.append(i)
            i+=1
            return mcd(a,b,l,i)
         else:
            return l
    else:
        return a

def mcm(a,b,l):
     a=int(a)
     b=int(b)
     m=max(l)
     Mcm=a*b/m
     return Mcm


if __name__=="__main__":
    i=2
    l=[]
    a=str(input("Ingresa un número natural: "))
    b=str(input("Ingresa otro número natural: "))
    MCD=mcd(a,b,l,i)
    MCM=mcm(a,b,l)
    print("El mínimo común múltiplo es",MCM)




      


  
    
         
    
           