#Ordenar tres números
x1= int(input("ingresa primer numero"))
x2= int(input("ingresa segundo numero"))
x3= int(input("ingresa tercer numero"))

if x1 <= x2 and x1 <= x3:
           
        if x2 <= x3:
             print(str(x1),",",str(x2),",",str(x3))
        else: print(x1,",",x3,",",x2)
             
elif x2 <= x1 and x2 <= x3:
     
        if x1 <= x3:
            
              print( x2,",", x1, ",", x3)
        else: print(x2,",", x3, ",", x1)
        
elif x3 <= x1 and x3 <= x2:
        
        if x2 <= x1:
            
              print(x3,",", x2, ",", x1)
        else: print(x3,",", x1, ",", x2)

