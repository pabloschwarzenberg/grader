num = int(input("Mencione un numero de 4 digitos\n"))
u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10
print("{}M+{}C+{}D+{}U".format(m,c,d,u)) 