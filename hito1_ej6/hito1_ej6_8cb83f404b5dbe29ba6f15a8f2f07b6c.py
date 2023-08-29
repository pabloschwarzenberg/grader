#Ordenar tres números
st = int(input("Ingrese su primer número:")) 
nd = int(input("Ingrese su segundo número:")) 
rd = int(input("Ingrese su tercer número:")) 
Ma = max(st, nd, rd)
Me = min(st, nd, rd)
result = (st + nd + rd) - Ma - Me
print("El orden de sus números de menor a mayor es:" , Me, ", ", result, ", " , Ma)