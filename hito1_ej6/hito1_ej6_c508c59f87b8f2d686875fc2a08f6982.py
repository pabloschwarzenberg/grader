#Ordenar tres números
x = input("Ingrese numero: ")
y = input ("Ingrese numero: ")
z = input ("Ingrese numero: ")
if z<=y<=x :
    print (z,",",y,",",x)
else :
     if x<=y<=z :
      print(x,",",y,",",z)
     else : 
       if y<=x<=z : 
         print (y,",",x,",",z)
       else:
          if x<=z<=y :
            print (x,",",z,",",y)
          else :
              if y<=z<=x : 
                print (y,",",z,",",x)
              else:
                 z<=y<=x 
                 print (z,",",y,",",x)