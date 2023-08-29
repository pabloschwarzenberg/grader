#Cálculo del dígito verificador de un rut
A=int(input())
R1=A%10
A1=A//10
R2=A1%10
A2=A1//10
R3=A2%10
A3=A2//10
R4=A3%10
A4=A3//10
R5=A4%10
A5=A4//10
R6=A5%10
A6=A5//10
R7=A6%10
A7=A6//10
R8=A7%10

S1=R1*2
S2=R2*3
S3=R3*4
S4=R4*5
S5=R5*6
S6=R6*7
S7=R7*2
S8=R8*3
ST=S1+S2+S3+S4+S5+S6+S7+S8
Sz=ST%11
guion=11-Sz
if guion==11: guion=0
if guion==10: guion="k"
print("dv=",guion)