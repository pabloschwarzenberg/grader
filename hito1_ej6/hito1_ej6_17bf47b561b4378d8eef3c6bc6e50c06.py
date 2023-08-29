#Ordenar tres números        
A = int(input("Ingrese el primer numero"))
B = int(input("Ingrese el segundo numero"))
C = int(input("Ingrese el tercer numero"))
Ma = max(A,B,C)
Mi = min(A,B,C)
Med = (A+B+C)-(Ma+Mi)

print("los numeros ordenados de mayor a menor = {},{},{}".format(Mi,Med,Ma))