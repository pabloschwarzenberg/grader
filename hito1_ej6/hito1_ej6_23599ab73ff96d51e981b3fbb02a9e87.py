#Ordenar tres números
num_1=int(input("ingrese el primer numero: "))
num_2=int(input("ingrese el segundo numero: "))
num_3=int(input("ingrese el tercer numero: "))
if num_1==num_2 and num_2==num_3:
    print(num_1,",",num_2,",",num_3)
    print("todos los valores son iguales, no hay orden ascendente")
elif (num_1<num_2 and num_1<num_3):
    if num_2<num_3:
        print(num_1,",",num_2,",",num_3)
    else:
        print(num_1,",",num_3,",",num_2)
elif (num_2<num_1 and num_2<num_3):       
    if num_1<num_3:
        print(num_2,",",num_1,",",num_3)
    else:
        print(num_2,",",num_3,",",num_1)
elif (num_3<num_1 and num_3<num_2):
    if num_1<num_2:
        print(num_3,",",num_1,",",num_2)
    else:
        print(num_3,",",num_2,",",num_1)    
           
