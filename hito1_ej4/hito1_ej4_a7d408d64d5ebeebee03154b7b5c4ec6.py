n=int((input("Ingresar numero: ")))
binario=""
if n==2:
    print(10)
else:
    while n>1:
        r=n%2
        n//=2
        if r==1:
            binario+='1'
        if r==0:
            binario+='0'
binario+=str(n)
N=str(binario)
b=N[::-1]
print("Resultado=",b)