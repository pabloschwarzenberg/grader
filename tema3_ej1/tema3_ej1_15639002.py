# completa el código de la función
#suma de divisores
def suma_divisores(a):
    b=2
    c=1
    if a==1:
        c=c-1
        return c,False
    else:
        while a!=1:
            
            if (a%b)==0:
                if (a//b)==1 and a==b and (a%2)!=0:
                    c=c
                    break
                elif (a//b)==1 and a==b:
                    c=c+b
                    break
                else:
                    a=(a/b)
                    c=c+b
            else:
                b=(b+1)
        if c==1:
          return c,True
        else:
          return c,False

if __name__=="__main__":    
    a=int(input("ingrese el número:"))
    
    j=suma_divisores(a)
   
    print("la suma es",j,"")
    
