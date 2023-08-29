#Ordenar tres números
N1=int(input("ingrese primer numero:"))
N2=int(input("ingrese segundo numero:"))
N3=int(input("ingrese tercer numero:"))
Min=min(N1,N2,N3)
Max=max(N1,N2,N3)
Med=(N1+N2+N3)-Min-Max
print(Min,","Med",",Max",")