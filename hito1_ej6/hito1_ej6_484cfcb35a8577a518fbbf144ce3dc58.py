#Ordenar tres números
a = int(input(" inserte primer numero : "))

b = int(input(" inserte segundo numero : "))

c = int(input(" inserte tercer numero : "))


Ma = max(a,b,c)

Mi = min(a,b,c)

C = (a + b + c) - Ma - Mi

print("los numeros ordenados de menor a mayor son ", Mi ," , ", C ," , ", Ma)   
