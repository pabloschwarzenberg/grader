#Descomponer un número
numero = int(input("ingrese numero: "))
n = numero

d1 = numero%10
numero = numero//10

d2 = numero%10
numero = numero//10

d3 = numero%10
numero = numero//10

d4 = numero%10
numero = numero//10

if 0 <= n <10:
    resultado = str(d1) + 'U'
    
if 10 <= n <100:
    resultado = str(d2)+ 'D + ' + str(d1) + 'U'
    
if 100 <= n <1000:
    resultado = str(d3)+'C + '  + str(d2) + 'D + ' + str(d1)+'U'
    
if 1000 <= n <10000:
    resultado = str(d4)+'M + ' + str(d3)+ 'C + ' + str(d2)+ 'D + ' + str(d1) + 'U'
print(resultado)