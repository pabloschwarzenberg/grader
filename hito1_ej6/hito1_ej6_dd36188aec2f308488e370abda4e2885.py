#Ordenar tres números
print("Estimado usuario porfavor ingrese tres numeros")
x= eval(input("primer numero: "))
y= eval(input("segundo numero: "))
z= eval(input("tercer numero: "))

Ma= max(x,y,z)
Mi= min(x,y,z)

D =(x+y+z)-Ma-Mi

print("el orden ascendete es:",Mi,",",D,",",Ma)     