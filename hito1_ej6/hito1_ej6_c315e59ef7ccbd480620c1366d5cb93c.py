#Ordenar tres números
a=int(input("Escriba el primer numero: "))
b=int(input("Escriba el segundo numero: "))
c=int(input("Escriba el tercer numero: "))
minimo= min(a, b, c)
maximo= max(a, b, c)
medio=(a+b+c)-minimo-maximo
print(minimo,",", medio,",", maximo)
      