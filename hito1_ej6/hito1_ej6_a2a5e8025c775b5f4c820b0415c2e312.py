num_1=int(input("ingrese el primer numero. "))
num_2=int(input("ingrese el segundo numero. "))
num_3=int(input("ingrese el tercer  numero. ")) 
mayor = 0
menor = 0
suma = num_1+num_2+num_3
if num_1 >= num_2 and num_1>=num_3:
  mayor = num_1
if num_2 >= num_1 and num_2>=num_3:
  mayor=num_2
if num_3 >= num_2 and num_3>=num_1:
  mayor=num_3
if num_1<=num_2 and num_1<=num_3:
  menor = num_1
if num_2<=num_1 and num_2<=num_3:
  menor =num_2
if num_3<=num_2 and num_3<=num_1:
  menor=num_3
medio=suma-mayor-menor
print(menor,",",medio,",", mayor)

      