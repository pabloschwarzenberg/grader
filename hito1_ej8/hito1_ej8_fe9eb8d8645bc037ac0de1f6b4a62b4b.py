#Descomponer un número
N=int(input("numero: "))
M=N//(10**3)
C=N//(10**2)-10*M
D=(N//10)-100*M-10*C
U=N-1000*M-100*C-10*D
print(M,"M + ",C,"C + ",D,"D + ",U,"U")