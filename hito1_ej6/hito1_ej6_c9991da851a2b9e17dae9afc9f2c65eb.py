#Ordenar tres números
x= int(input("ingresar primer numero"))
y=int(input("ingresar segundo numero"))
w=int(input("ingresar tercer numero"))

if x<=y<=w:
    print ("los numeros ordenados son: ", x,',',y,',',w)
    
if x<=w<=y:
  print ("los numeros ordenados son: ", x,',',w,',',y)
  
if y<=x<=w:
  print ("los numeros ordenados son: ",  y,',',x,',',w)
  
if y<=w<=x:
  print ("los numeros ordenados son: ",  y,',',w,',',x)
  
if w<=x<=y:
  print ("los numeros ordenados son: ",  w,',',x,',',y)
  
if w<=y<=x:
  print ("los numeros ordenados son: ",  w,',',y,',',x)
  

  