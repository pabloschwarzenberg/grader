s=int(input("Ingrese un número: "))
numero=0
f=True;
for k in range(0,len(s)):
    if int(s[k])%2==1:
        f=False;
        break;
if f:
    print("es par")
else:
    print("No es par")

           