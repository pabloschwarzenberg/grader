'''
Ordena 3 numeros e imprimelos de menor a mayor separados por una coma
A B C
A C B
B A C
B C A
C A B
C B A
'''

num_1 = int(input("ingrese el primer numero: "))
num_2 = int(input("ingrese el segundo numero: "))
num_3 = int(input("ingrese el tercero numero: "))

if( (num_1 <= num_2) and (num_1 <= num_3)):
    if(num_2 < num_3):
        print(str(num_1)+","+str(num_2)+","+str(num_3))
    else:
        print(str(num_1)+","+str(num_3)+","+str(num_2))
elif((num_2 <= num_1) and (num_2 <= num_3)):
    if(num_1 <= num_3):
        print(str(num_2)+","+str(num_1)+","+str(num_3))
    else:
        print(str(num_2)+","+str(num_3)+","+str(num_1))
elif((num_3 <= num_1) and (num_3 <= num_2)):
    if(num_1 <= num_2):
        print(str(num_3)+","+str(num_1)+","+str(num_2))
    else:
        print(str(num_3)+","+str(num_2)+","+str(num_1))
