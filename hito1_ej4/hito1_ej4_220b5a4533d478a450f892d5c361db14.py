n=int(input("Ingrese un numero decimal: "))
x=n
k=[]
while (n>0):
    a=int(float(n%2))
    print("valor de a :",a)
    k.append(a)
    n=(n-a)/2
k.append(0)
string=""
for j in k[::-1]:
    string=string+str(j)
print("El numero decimal %d equivale en binario a %s" %(x, string))