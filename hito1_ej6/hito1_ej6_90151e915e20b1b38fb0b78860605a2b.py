#Ordenar tres números
import math
print("ingresa 3 numero de un digito de tu preferencia")
num_1 = input()
num_2 = input()
num_3 = input()

if num_1<=num_2 and num_2<=num_3 :
    print(num_1 ,",", num_2 ,",", num_3)
    
if num_1>=num_2 and num_2>=num_3 :
    print(num_3 ,",", num_2 ,",", num_1)
    
if num_2>=num_1 and num_2>=num_3 and num_3>=num_1:
    print(num_1 ,",", num_3 ,",", num_2)
    
if num_2>=num_1 and num_2>=num_3 and num_3<=num_1:
    print(num_3 ,",", num_1 ,",", num_2)
    
if num_2<=num_1 and num_2<=num_3 and num_1<=num_3:
    print(num_2 ,",", num_1 ,",", num_3)