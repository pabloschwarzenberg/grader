#Descomponer un número
n=str(input("Ingrese número:"))
m=len(n)-1
print(int(n[m-3]),"M+",int(n[m-2]),"C+",int(n[m-1]),"D+",int(n[m]),"U")      