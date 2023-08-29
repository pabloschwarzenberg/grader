n=int(input("Ingrese un numero decimal: "))
x=n
k=[]
while (n>0):
    a=int(float(n%2))
    k.append(a)
    n=(n-a)/2
k.append(0)
string=""
for j in k[::-1]:
    string=string+str(j)
binario = int(string)
binariostr = str(binario)
print("resultado="+binariostr)