#Ordenar tres números
#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
#Variables A, B, C para guardar de mayor a menor
A=0
B=0
C=0
#Solicita variables
N1=int(input("Ingrese el primer número \n"))
N2=int(input("Ingrese el segundo número \n"))
N3=int(input("Ingrese el tercer número \n"))
#Ordena números - Acepta nros iguales
if(N1>=N2) and (N1>=N3):
  A=N1
if(N1<=N2) and (N1>=N3) or (N1>=N2) and (N1<=N3):
  B=N1
if(N1<=N2) and (N1<=N3):
  C=N1
if (N2>=N1) and (N2>=N3):
  A=N2
if (N2>=N1) and (N2<=N3) or (N2<=N1) and (N2>=N3):
  B=N2
if (N2<=N1) and (N2<=N3):
  C=N2
if (N3>=N1) and (N3>=N2):
  A=N3
if (N3>=N1) and (N3<=N2) or (N3<=N1) and (N3>=N2):
  B=N3
if (N3<=N1) and (N3<=N2):
  C=N3
print ("de mayor a menor, sus número son: ", C, ",", B, ",", A)