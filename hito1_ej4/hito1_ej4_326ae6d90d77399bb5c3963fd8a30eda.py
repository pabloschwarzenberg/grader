#CONVERSOR DE DECIMAL A BINARIO 
numero=int(input("Ingrese un número: "))
binario=[]
while numero>0:
    a=int(float(numero%2))
    binario.append(a)
    numero=(numero-a)/2
string=""
for j in binario[::-1]:
    string=string+str(j)
print("resultado=",string)