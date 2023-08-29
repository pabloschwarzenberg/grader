#Ordenar tres números
nums = input("Ingrese tres números enteros separados por espacios: ")
nums = [int(num) for num in nums.split()]
nums.sort()
print(nums[0], nums[1], nums[2], sep=",")