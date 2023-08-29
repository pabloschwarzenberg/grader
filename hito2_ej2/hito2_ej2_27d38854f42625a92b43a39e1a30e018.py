dicc="ACTG"
n=str(input(":"))
c=0
for x in n:
    if x not in dicc:
        c+=1
if c!=0:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")

   