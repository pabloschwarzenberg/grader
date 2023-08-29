#ordenar tres numeros de menor a mayor con comas

a= int(input( "ingrese numero = "))
b= int(input( "ingrese numero = "))
c = int(input( "ingrese numero = "))

#definir el menor de los numeros 
if   a<= b and  a<= c  :
        Nmenor = a
elif  b < a  and b < c :
       Nmenor = b
else:
        Nmenor = c

print("el numero menor es " , Nmenor )
 
 # definir el numero mayor 
if  b>=a and b>=c:
     Nmayor = b
else :
    Nmayor = c

print("el numero mayor es ", Nmayor)

#definir el numero del medio

if b>=c and c>=a:
        Nmedio = c
elif a>c and b>a :
        Nmedio  = a

else :
        Nmedio = b

print("el numero del medio es " , Nmedio)


#salida

print(Nmenor, " , " , Nmedio , "," , Nmayor)