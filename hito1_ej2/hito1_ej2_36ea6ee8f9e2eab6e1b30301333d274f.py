#Contestador de celular
x= input("Ingrese numero telefonico:")
y= input("Ingrese hora de la llamada:")


k= str(x)
AB= k[5]
AC= k[6]
AD= k[7]

b= k[0]
v= k[1]
n= k[2]

p= str(y)

if (y==str(00)) or (y==str(0)) or (y==str(1)) or (y==str(2)) or (y==str(3)) or (y==str(4)) or (y==str(5))or (y==str(6)) or (y==str(7)):
    print("Resultado: CONTESTAR")
    
else:
    if (AB==str(9)) and (AC==str(0)) and (AD==str(9)) and (y==str(8)) and (y==str(9)) or (y==str(10)) or (y==str(11)) or (y==str(12)) or (y==str(13)):
      print("Resultado: CONTESTAR")
      
    else:
         if (b==str(8)) and (v==str(7)) and (n==str(7)) and (y==str(17)) or (y==str(18)) or (y==str(19)):
            print("Resultado: NO CONTESTAR")
            
         else:
             if (y==str(17)) or (y==str(18)) or (y==str(19)):
                    print("Resultado: CONTESTAR")
                    
             else:
                 if (y==str(19)) or (y==str(20)) or (y==str(21)) or (y==str(22)) or (y==str(23)):
                     print("Resultado: NO CONTESTAR")