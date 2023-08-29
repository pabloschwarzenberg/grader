#Descomponer un número
num = int(input())
d = len(str(num))

for i in range(1 ,d + 1):
    if i == 1:
        salida = str(num % 10) + 'U'
    
    elif i == 2:
        salida = str(num % 10) + 'D ' + "+ " + salida
        
    elif i == 3:
        salida = str(num % 10) + 'C ' + "+ " + salida
        
    else:
        salida = str(num % 10) + 'M ' + "+ " + salida
        
    num = num//10
        

print(salida)