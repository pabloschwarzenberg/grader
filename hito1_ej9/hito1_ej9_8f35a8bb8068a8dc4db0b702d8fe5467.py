print ("Escriba su primera ecuación, que será de la forma ax + by = e")
       
a = eval(input("Ingrese A:"))
b = eval(input("Ingrese B:"))    
e = eval(input("Ingrese E:"))

print ("Escriba su segunda ecuación, que será de la forma cx + dy = f")
       
c = eval(input("Ingrese C:"))
d = eval(input("Ingrese D:"))    
f = eval(input("Ingrese F:"))

denominador = (a*d - b*c)
if denominador == 0: 
 print ("La ecuación no tiene solución") 

else:
     
   x = (e*d - b*f)/(a*d - b*c)
   y = (a*f - e*c)/(a*d - b*c)
  
   round (x)
   round (y)
   
   print ("x=",x)
   print ("y=",y)

     
