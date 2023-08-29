#Ordenar tres números
A= eval(input("Ingrese un numero:"))
E=eval(input("Ingrese un segundo numero:"))
I=eval(input("Ingrese un tercer numero:"))
Ma =max(A,E,I)
Mi =min(A,E,I)
O= (A+E+I)-Ma-Mi
print("De menor a mayor su orden es ", Mi ," , ", O ," ,", Ma)