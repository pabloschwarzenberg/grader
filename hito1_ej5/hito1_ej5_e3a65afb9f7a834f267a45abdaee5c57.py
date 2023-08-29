#Cálculo del dígito verificador de un rut
r=int(input("ingrese rut: ",))
d1=r%10
d2=r%100//10
d3=r%1000//100
d4=r%10000//1000
d5=r%100000//10000
d6=r%1000000//100000
d7=r%10000000//1000000
d8=r%100000000//10000000
d9=r%1000000000//100000000
Z=(d1*2)+(d2*3)+(d3*4)+(d4*5)+(d5*6)+(d6*7)+(d7*2)+(d8*3)+(d9*4)
C=int((Z)/11)
X=Z-(11*C)
V=11-X
if (V==11):
    print("dv=0")
elif (V==10):
    print("dv=K")
else:
    print("dv=",V)
