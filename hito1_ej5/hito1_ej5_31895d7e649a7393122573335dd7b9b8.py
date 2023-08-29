#Cálculo del dígito verificador de un rut
R= (input("ingrese su rut"))

n1= int(R[-1]) * 2
        
n2= int (R[-2]) * 3

n3= int (R[-3]) * 4

n4= int (R[-4]) * 5 

n5= int (R[-5])* 6 

n6= int (R[-6]) * 7 

n7= int (R[-7]) * 2
if (len(R)==8):
    n8= int(R[-8]) * 3



if(len(R)== 7):
 
    SUMA= int(n1 + n2 + n3 + n4 + n5 + n6 + n7)
    ENTERO= int(SUMA//11)
    RESTO= int(SUMA - (11*ENTERO))
    VARIABLE= int(11-RESTO)
    #print(SUMA,ENTERO,RESTO,VARIABLE)

    if (VARIABLE == 11):
        print("dv=0")

    if (VARIABLE == 10):
        print("dv=k")

    if (VARIABLE!=11) and (VARIABLE!=10):
        print("dv=",VARIABLE)
    


    
if(len(R)== 8):
    SUMA= int(n1 + n2 + n3 + n4 + n5 + n6 + n7+ n8)  
    ENTERO= int(SUMA//11)
    RESTO= int(SUMA - (11*ENTERO))
    VARIABLE= int(11 - RESTO)
    #print(SUMA,ENTERO,RESTO,VARIABLE)
  
  
    if (VARIABLE == 11):
        print("dv=0")

    if (VARIABLE == 10):
        print("dv=k")

    if (VARIABLE!=11) and (VARIABLE!=10):
        print("dv=", VARIABLE)
