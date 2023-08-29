#Factores Primos
list = [2,3,5,7,11,13]
list2 = []
n = int(input("Ingrese el numero: "))
r= n
while(n !=1):
    if (n % list[0] == 0):
        n = n / list[0]
        list2.append(list[0])
    if (n % list[1] == 0):
        n = n / list[1]
        list2.append(list[1])
    if (n % list[2] == 0):
        n = n / list[2]
        list2.append(list[2])
    if (n % list[3] == 0):
        n = n / list[3]
        list2.append(list[3])
    if (n % list[4] == 0):
        n = n / list[4]
        list2.append(list[4])
    if (n % list[5] == 0):
        n = n / list[5]
        list2.append(list[5])
print(list2)
for i in list2:
    print(i)