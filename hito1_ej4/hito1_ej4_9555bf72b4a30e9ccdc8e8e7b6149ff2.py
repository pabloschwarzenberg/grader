import math
n=int(input("Base 10: "))
b=1
a=0

while n>0:
    b=math.log2(n)
    a=10**int(b)+a      #Genera binario
    n=n-2**int(b)

a=a
print("resultado=",a)