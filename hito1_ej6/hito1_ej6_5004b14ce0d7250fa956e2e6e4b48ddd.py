#Ordenar tres números
P= eval(input("Ingrese un numero: "))
Q= eval(input("Ingrese un segundo numero: "))
R= eval(input("Ingrese un tercer numero: "))
Mx= max(P,Q,R)
Mn= min(P,Q,R)
T= (P+Q+R)- Mx -Mn
print("El orden de los numeros de menor a mayor es", Mn , "," , T , "," , Mx)