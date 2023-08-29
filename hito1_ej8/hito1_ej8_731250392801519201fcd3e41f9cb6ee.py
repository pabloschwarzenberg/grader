#Descomponer un número
N=int(input())
A = N//1000
B= (N//100) - 10*A
C= (N//10)-(100*A + 10*B)
D= N - (1000*A + 100*B + 10*C)
print(A,"M","+",B ,"C","+",C,"D","+",D,"U",)