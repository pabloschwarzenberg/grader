secuencia= input("Escriba la secuencia")
i=0
mensaje=0
while i in secuencia:
    if i==A or i==C or i==T or i==G:
        mensaje= 1
    else:
        mensaje= 2
    i= i+1

if mensaje==1:
    print("Secuencia correcta")
if mensaje==2:
    print("Secuencia incorrecta")