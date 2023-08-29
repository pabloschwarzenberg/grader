#Ordenar tres números
nums=[]
for i in range(3):
    num=int(input("Ingresa un número: "))
    nums.append(num)
    nums.sort()  
    
print("Números ordenados de menor a mayor:")
for num in nums:
    print(f"{num},",end="")