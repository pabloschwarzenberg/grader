#Ordenar 3 números
N1 = int(input("Ingrese el Primer Número: "))
N2 = int(input("Ingrese el Segundo Número: "))
N3 = int(input("Ingrese el Tercer Número: "))
Ma = max(N1,N2,N3)
Mi = min(N1,N2,N3)
H = (N1 + N2 + N3) - Ma - Mi     
print(Mi ," , ", H ,", ",Ma)