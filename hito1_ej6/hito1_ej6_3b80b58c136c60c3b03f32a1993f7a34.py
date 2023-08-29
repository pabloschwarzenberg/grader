a=int(input("Escriba primer numero: "))
b=int(input("Escriba segundo numero: "))
c=int(input("Escriba tercer numero: "))
minimo= min(a, b, c)
maximo= max(a, b, c)
medio=(a+b+c)-minimo-maximo
print(minimo,",", medio,",", maximo)