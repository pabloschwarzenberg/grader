#Ordenar tres números
x= int(input("escriba el primer numero:"))
y= int(input("escriba el segundo numero:"))
z= int(input("escriba el tercer numero:"))

menor = min(x,y,z)
mayor= max(x,y,z)
b= (x + y + z)-mayor-menor

print(menor,",", b ,",", mayor)
