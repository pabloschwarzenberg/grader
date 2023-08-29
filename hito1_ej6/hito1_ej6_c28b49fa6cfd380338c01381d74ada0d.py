#Ordenar tres números
print("te ordenare 3 numeros que elijas de menor a mayor")
x=int(input("inserta tu primer numero:"))
y=int(input("inserta tu segundo numero:"))
z=int(input("inserta tu tercer numero"))
mo=min(x,y,z)
mx=max(x,y,z)
me=(x+y+z)-mo-mx
print("el orden de los numeros de menor a mayor es:",mo,",",me,",",mx)