n=str(input("ingrese un numero: "))
largo=len(n)
mensajeM=(n[0],"M")
mensameMC=(n[0],"M +",n[1],"C")
mensajeMCD=(n[0],"M +",n[1],"C +",n[2],"D")
mensaje=(n[0],"M +",n[1],"C +",n[2],"D +",n[3],"U")

if largo==1:
    print(mensajeM)
if largo==2:
    print(mensajeMC)
if largo==3:
    print(mensajeMCD)
if largo==4:
    print(mensaje)