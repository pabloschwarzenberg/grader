import random
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
matrizAlfabeto=[None]*(10)
palabra1=["P","O","G","R","A","M","A","R"]
palabra2=["V","A","R","I","A","B","L","E"]
for i in range(0,10):
    matrizAlfabeto[i] = [None]*10
for i in range(10):
    for j in range(10):
        matrizAlfabeto[i][j] = alfabeto[random.randint(o,25)]

for i in range(8):
    matrizAlfabeto[i][0]=palabra1[i];
    matrizAlfabeto[9][i]=palabra2[i];
print(matrizAlfabeto)