#Ingresa 1ra variable

N1 = eval(input("Ingrese su primer numero "))

#Ingresa 2da Variable

N2= eval(input("Ingrse su segundo numero "))

#Ingresa 3era variable

N3 = eval(input("Ingrese su tercer numero"))

#Menor a mayor

MA = max(N1,N2,N3)
MI = min(N1,N2,N3)
D = (N1 + N2 + N3) - MA - MI

#Salida

print("Orden de menor a mayor:", MI ," , " , D , " , " , MA ,".")