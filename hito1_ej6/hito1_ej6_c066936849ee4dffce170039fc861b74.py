num_1=int(input("Escribe el número 1: "))
num_2=int(input("Escribe el número 2: "))
num_3=int(input("Escribe el número 3: "))

if num_1>=num_2>=num_3:
   print(num_3,",",num_2,",",num_1)
elif num_3>=num_2>=num_1:
   print(num_1,",",num_2,",",num_3)
elif num_1>=num_3>=num_2:
   print(num_2,",",num_3,",",num_1)
elif num_2>=num_1>=num_3:
   print(num_3,",",num_1,",",num_2)
elif num_2>=num_3>=num_1:
   print(num_1,",",num_3,",",num_2)
elif num_3>=num_1>=num_2:
    print(num_2,",",num_1,",",num_3)