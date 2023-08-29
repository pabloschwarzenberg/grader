#Ordenar tres números

N1 = eval(input("Ingrese su primer numero: "))


N2= eval(input("Ingrse su segundo numero: "))


N3 = eval(input("Ingrese su tercer numero: "))


MA = max(N1,N2,N3)
MI = min(N1,N2,N3)
D = (N1 + N2 + N3) - MA - MI

print("Orden de menor a mayor:", MI ," , " , D , " , " , MA ,".")