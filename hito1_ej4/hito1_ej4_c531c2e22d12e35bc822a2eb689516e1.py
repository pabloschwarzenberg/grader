n=int(input("Ingrese un número: ")) 
z=[] 
while n>0: 
    a=int(float(n%2)) 
    z.append(a) 
    n=(n-a)/2 
string="" 
for j in z[::-1]: 
    string=string+str(j) 
print("resultado=",string)
