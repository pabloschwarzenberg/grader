'''
Escribe un programa que reciba como entrada un número decimal e imprima el resultado de convertirlo a binario. Por ejemplo, al ingresar el número 33 tu programa debiera imprimir el siguiente mensaje:

resultado=100001
'''
num = int(input('Ingrese el numero a convertir: '))
num_temp = num
binario = ""
while num_temp != 1:
    binario = binario + str(num_temp%2)
    num_temp = num_temp//2
binario = binario+str(num_temp)
binario_tmp = ""

for i in range(0,len(binario)):
    binario_tmp = binario_tmp+binario[len(binario)-1-i]

binario = binario_tmp
print("resultado="+binario)