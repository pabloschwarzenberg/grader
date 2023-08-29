n=str(input("ingrese cadena:"))
u=n.upper()
suma=0
c=0
for i in range(len(u)):
        if u[i]!="A" and u[i]!="C" and u[i]!="G" and u[i]!="T" :
            c=c+1
            
if suma<c:
    print("secuencia incorrecta")
if suma==c:
    print("secuencia correcta")
        