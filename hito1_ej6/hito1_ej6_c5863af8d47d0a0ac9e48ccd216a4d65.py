#Ordenar tres números
x= int(input("Primer Numero: "))
y= int(input("Segundo Numero: "))   
z= int(input("Tercer Numero: "))   

a= min(x,y,z)
c= max(x,y,z)
b= (x+y+z)-a-c

print("Los numeros ordenados son: {}, {} , {}".format(a,b,c))
          