#Descomponer un número
numero= int(input("Digite un numero de 4 digitos\n"))
u = numero // 1 % 10
d = numero // 10 % 10 
c = numero // 10**2 % 10
m = numero // 10**3 % 10
print("{}M+{}C+{}D+{}U".format(m,c,d,u))
      