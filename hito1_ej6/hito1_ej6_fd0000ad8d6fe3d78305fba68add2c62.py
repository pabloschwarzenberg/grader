#Ordenar tres números
x=int(input("escriba el primer numero: "))
y=int(input("escriba el segundo numero: "))
z=int(input("escribaa el tercer numero: "))

Ma = max(x,y,z)
print("el numero mayor es: ", Ma)
Mi = min(x,y,z)
print("el numero menos es: ", Mi)

O =(x + y + z) - Ma - Mi

print("los numero ordenados de menor a mayor son ", Mi,",", O,",",Ma)      