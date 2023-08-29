#Ordenar tres números
a = eval(input("Ingrese un numero: "))

b = eval(input("Ingrese un segundo numero: "))

c = eval(input("Ingrese un tercer numero: "))



Ma = max(a,b,c)

Me = min(a,b,c)



D = (a + b + c) - Ma - Me



print("De menor a mayor el órden es ", Me ," , ", D , " , ", Ma)      