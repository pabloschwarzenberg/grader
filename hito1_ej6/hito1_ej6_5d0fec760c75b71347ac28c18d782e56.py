#Ordenar tres números
x = int(input("Ingresa un valor para x: "))
y = int(input("Ingresa un valor para y: "))
z = int(input("Ingresa un valor para z: "))
print("sus numeros seran ordenados de mayor a menor a continuacion")
if x<=y<=z:
    print(x,str(","),y,str(","),z)    
elif x<=z<=y:
    print(x,str(","),z,str(","),y)    
elif z<=x<=y:
    print(z,str(","),x,str(","),y)    
elif z<=y<=x:
    print(z,str(","),y,str(","),x)    
elif y<=x<=z:
    print(y,str(","),x,str(","),z)    
elif y<=z<=x:
    print(y,str(","),z,str(","),x)