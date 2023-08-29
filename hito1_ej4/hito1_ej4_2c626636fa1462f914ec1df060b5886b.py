x=int(input("Ingrese un numero decimal:"))
y=x
z=[]
while x>0:
  a=int(float(x%2))
  z.append(a)
  x=(x-a)/2
z.append(0)
string=""
for j in z[::-1]:
  string=string+str(j)
print("Resultado=",(string[1:]))
