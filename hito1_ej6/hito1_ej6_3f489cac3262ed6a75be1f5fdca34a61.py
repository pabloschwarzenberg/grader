#Ingresa una variable

x = eval(input("Ingrese su primer numero "))

#Ingresa la segunda Variable
y = eval(input("Ingrse su segundo numero "))
#Ingresa la 3era variable
z = eval(input("Ingrese su tercer numero"))

#Mayor a menor

MA = max(x,y,z)

MI = min(x,y,z)

D = (x + y + z) - MA - MI



print("Este es el orden de los numeros de menor a mayor", MI ," , " , D , " , ",MA,"." )