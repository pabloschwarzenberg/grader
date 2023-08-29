#Descomponer un número
num=int(input("Ingrese número: "))
tipo=1
cadena=""
while 0<num<10000:
    resto=num%10
    num=num//10
    if tipo==1:
        un="U"
    elif tipo==2:
        un="D + "
    elif tipo==3:
        un="C + "
    elif tipo==4:
        un="M + "
    cadena=str(resto)+un+cadena
    tipo+=1
print(cadena)