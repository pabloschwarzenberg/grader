#Factores Primos
x = int(input("Ingresa un número: "))
i=2
L=[]
R=[]
while i <= x:
    if x%i==0:
        L.append(i)
    i=i+1
for num in L:
    i=2
    if num==2:
        print(2)
    while i < num:
        if num%i==0:
            break
        if num-1==i:
            print(num)
        i=i+1
