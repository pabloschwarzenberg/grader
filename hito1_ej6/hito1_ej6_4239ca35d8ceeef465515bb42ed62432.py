#Ordenar tres números
x=int(input("ingrese numero"))
y=int(input("ingrese numero"))
z=int(input("ingrese numero"))
ma=max(x,y,z)
mi=min(x,y,z)
me=(x+y+z)-ma-mi
print(mi,",",me,",",ma)
  
