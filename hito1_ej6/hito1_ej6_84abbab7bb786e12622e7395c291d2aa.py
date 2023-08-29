#Ordenar números
n1=input("Ingrese el primer numero:")
n1=int(n1)
n2=input("Ingrese el segundo numero:")
n2=int(n2)
n3=input("Ingrese el tercer numero:")
n3=int(n3)
print('Ordenados de mayor a menor, los numeros son los siguientes:')
if n1>=n2 and n2>=n3:
    print(n3,',',n2,',',n1)
if n1>=n3 and n3>=n2:
    print(n2,',',n3,',',n1)

if n2>=n1 and n1>=n3:
    print(n3,',',n1,',',n1)
if n2>=n3 and n3>=n1:
    print(n1,',',n3,',',n2)
if n3>=n1 and n1>=n2:
    print(n2,',',n1,',',n3)
if n3>=n2 and n2>=n1:
    print(n2,',',n1,',',n3)

      