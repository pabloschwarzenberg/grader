num1=int(input("--> ingrese el primer numero --> :"))
num2=int(input("--> ingrese el segundo numero --> : "))
num3=int(input("--> ingrese el terecer numero --> : "))
A=min(num1,num2,num3)
C=max(num1,num2,num3)
B=(num1+num2+num3)-A-C
print("¡¡LOS NUMEROS INGRESADOS HAN SIDO ORDENADOS!! : {},{},{}".format(A,B,C))