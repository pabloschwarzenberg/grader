#Ordenar tres números
list1= []
while (len(list1)<3):
    nums=int(input("porfavor ingrese 3 numeros, uno a uno, para que estos seqan ordenados de mayor a menor: "))
    list1.append(nums)
list1.sort()
print("ordenados de mayor a menor serian:" , list1)