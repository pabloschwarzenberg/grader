# completa el código de la función
def amigos(a,b):
    sumaA=0
    i=1
    while i<a:
        resto=a%i
        if resto==0:
            print(i,end=" ")
            sumaA=sumaA+i
            i=i+1
        else:
            i=i+1
            continue
    sumaB= 0
    j = 1
    while j < b:
        resto = b % j
        if resto == 0:
            print(j,end=" ")
            sumaB = sumaB + j
            j = j + 1
        else:
            j = j + 1
            continue
    if sumaA==b and sumaB==a:
        return True
    else:
        return False
    

 
  
  
 

