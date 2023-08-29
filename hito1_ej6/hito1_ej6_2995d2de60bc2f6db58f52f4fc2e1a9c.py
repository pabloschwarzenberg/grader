#Ordenar tres números
 
a= int(input("escriba un numero: "))
b= int(input("escriba otro numero: "))
c= int(input("escriba otro numero: "))
 
d= min(a,b,c)
f= max(a,b,c)
e= (a+b+c)-d-f
      
print("los numeros ordenados son: {},{},{}".format(d,e,f))