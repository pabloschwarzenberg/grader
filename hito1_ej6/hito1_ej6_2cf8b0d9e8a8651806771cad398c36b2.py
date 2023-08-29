#Ordenar tres números 
total_numbers = 3
num = []
 
for i in range(total_numbers):
    num.append(int(input("Ingresa el número #{}: ".format(i+1))))
 
for i in range(total_numbers-1):
    for j in range(i+1,total_numbers):
        if(num[i] > num[j]):
            cambio = num[i]
            num[i] = num[j]
            num[j] = cambio

string_list = ','.join(str(n) for n in num)
print("Numeros ordenados de menor a mayor: ", string_list)