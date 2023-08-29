#Descomponer un número
x=input("Ingrese numero de hasta 4 digitos ")
y=int(x)
if y>=1000:
    print(x[0]+"M + "+x[1]+"C + "+x[2]+"D + "+x[3]+"U")
elif y>100:
    print(x[0]+"C + "+x[1]+"D + "+x[2]+"U")
elif y>10:
    print(x[0]+"D + "+x[1]+"U")
else:
    print(x[1]+"U")
