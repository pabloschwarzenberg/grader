q=int(input("Ingrese un numero decimal: "))
w=q
k=[]
while (q>0):
    a=int(float(q%2))
    k.append(a)
    q=(q-a)/2
string=""
for p in k[::-1]:
    string=string+str(p)
print("al igresar %d resultado= %s" %(w, string))