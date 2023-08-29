num_1 = eval(input("Ingrese el primer número:"))
num_2 = eval(input("Ingrese el segundo número:"))
num_3 = eval(input("Ingrese el tercer número:"))
if(num_1 <= num_2 and num_2 <= num_3):
    print(num_1, (","),num_2, (","),num_3)
if(num_1 <= num_2 and num_3 <= num_2):
    print(num_1, (","),num_3, (","),num_2)
if(num_2 <= num_1 and num_1 <= num_3):
    print(num_2, (","),num_1, (","),num_3)
if(num_2 <= num_1 and num_3 <= num_1):
    print(num_2, (","),num_3, (","),num_1)
if(num_3 <= num_1 and num_1 <= num_2):
    print(num_3, (","),num_1, (","),num_2)