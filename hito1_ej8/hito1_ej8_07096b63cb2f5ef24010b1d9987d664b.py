# ingreso
N = int(input("ingresa numero: "))
# determinar milesima
M = int(N/1000)
# determinar centesima
C = (N-1000*M)
C = (C/100)
C = int(C)
# determinar decima
D = (N-(1000*M+C*100))
D = (D/10)
D = int(D)
# determinar unidad
U = (N-(1000*M+C*100+D*10))
# imprimir
print(M,"M +" ,C,"C +",D,"D +",U,"U")