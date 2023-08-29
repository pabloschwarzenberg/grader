#Ordenar tres números
n1=int(input("ingrese primer numero"))
n2=int(input("ingrese segundo numero"))
n3=int(input("ingrese tercer numero"))
ma= max(n1,n2,n3)
mi= min(n1,n2,n3)
d= (n1+n2+n3)-ma-mi
print("De menor a mayor el orden es ", mi ," , ", d , " , ", ma) 