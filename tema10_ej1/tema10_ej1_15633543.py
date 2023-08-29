def mcm(a,b,ab):
    r = a%b
    if r == 0:
       respuesta = ab/b
       return respuesta
    else:
        mcm(b,r,ab)
    

if __name__=="__main__":
    num1 = int(input("ingrese numero: "))
    num2 = int(input("ingrese otro numero: "))
    mcm(num1,num2,num1*num2)
    
    
           