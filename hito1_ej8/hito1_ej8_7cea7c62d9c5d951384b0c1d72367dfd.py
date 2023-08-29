#Descomponer un número
numero= int(input("ingrese un digito de 4 cifras: "))
M=(numero//1000)
M2=(numero%1000)
C=(M2//100)
C2=(M2%100)
D=(C2//10)
D2=(C2%10)
U=(D2//1)
print("M",M,"C",C,"D",D,"U",U)
   