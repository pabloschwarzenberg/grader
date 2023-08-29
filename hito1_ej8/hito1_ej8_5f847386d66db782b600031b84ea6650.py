#Descomponer un número
A = int(input("inserte cualquer numero:"))
A = str(A)
N = len(A)
if N == 4:
 print (A[0] , "M +", A[1] , "C +",A[2], "D +", A[3], "U")
elif N == 3:
 print(A[0] , "C +", A[1], "D +", A[2], "U ")
elif N == 2:
 print(A[0], "D +", A[1], "U ")
elif N == 1:
 print(A[0], "U ")