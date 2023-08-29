#Ordenar tres números
print("Escriba tres numeros para que luego sean ordenandos de menor a mayor.")

n1=int(input("Escriba el primer numero: "))
n2=int(input("Escriba el segundo numero: "))
n3=int(input("Escriba el tercer numero: "))
max=0
min=0
mid=0

if n1>n2 and n1>n3  :
    max=n1
    if n2>n3:
        min=n3
        mid=n2
        print(min, ",", mid, ",", max)
    else:
        min=n2
        mid=n3
        print(min, ",", mid, ",", max)

elif n2>n1 and n2>n3:
    max=n2
    if n1>n3:
        min=n3
        mid=n1
        print(min, ",", mid, ",", max)
    else:
        min=n1
        mid=n3
        print(min, ",", mid, ",", max)

elif n3>n1 and n3>n2:
    max=n3
    if n2>n1:
        min=n1
        mid=n2
        print(min, ",", mid, ",", max)
    else:
        min=n2
        mid=n1
        print(min, ",", mid, ",", max)

elif n1==n2 and n1>n3:
    max=n1
    mid=n2
    min=n3
    print(min, ",", mid, ",", max)

elif n3==n1 and n3>n2:
    max=n3
    mid=n1
    min=n2
    print(min, ",", mid, ",", max)

elif n2==n3 and n3>n1:
    max=n2
    mid=n3
    min=n1
    print(min, ",", mid, ",", max)

else:
    print("Los numeros que ingresaste son pares...")