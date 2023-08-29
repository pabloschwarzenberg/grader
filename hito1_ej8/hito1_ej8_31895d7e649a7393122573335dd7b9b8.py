#Descomponer un número
N=input("ingrese un numero de hasta 4 digitos")

LN= len(N)
if(LN==4):
    u= N[3]
    d= N[2]
    c= N[1]
    m= N[0]
    print(m,"M +",c,"C +",d,"D +",u,"U")

if(LN==3):
    u= N[2]
    d= N[1]
    c= N[0]
   
    print(c,"C +",d,"D +",u,"U")

    
if(LN==2):
    u= N[1]
    d= N[0]
   
    print(d,"D +",u,"U")
    
if(LN==1):
    u= N[0]
    
    print(u,"U")



