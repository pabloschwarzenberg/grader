nums = [int(input("Ingrese el número {}: ".format(i+1))) for i in range(3)]
nums.sort()
print("Los números ordenados son:", ", ".join(map(str, nums)))