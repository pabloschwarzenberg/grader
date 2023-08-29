#Ordenar tres números
cant_num=3
may_men=[]

for i in range(cant_num):
    numero=int(input("Ingrese un numero entero:"))
    may_men.append(numero)

may_men.sort()
print(may_men)