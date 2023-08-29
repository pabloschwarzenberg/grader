#Conversor de Decimal a Binario
n = int(float(input()))
b = bin(n)
b_1=list(b)
b_1.pop(0)
b_1.pop(0)
b_2= "".join(b_1)
print("resultado=",b_2)