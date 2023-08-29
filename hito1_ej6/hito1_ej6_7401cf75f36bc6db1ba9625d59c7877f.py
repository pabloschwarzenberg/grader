x = int(input("Coloca aca tu primer numero: "))   
y = int(input("Coloca aca tu primer numero: "))
z = int(input("Coloca aca tu primer numero: ")) 

a = min(x, y, z)  
c = max(x, y, z) 
b = (x + y + z) - a - c 

print("Los numeros de menor a mayor son: {}, {}, {}".format(a, b, c)) 