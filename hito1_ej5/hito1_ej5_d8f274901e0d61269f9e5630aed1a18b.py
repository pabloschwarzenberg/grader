#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese un rol único tributario: "))

#Formula digito x digito
pd = (rut//10000000)
sd = ((rut//1000000)%10)
td = ((rut//100000)%10)
cd = ((rut//10000)%10)
qd = ((rut//1000)%10)
sed = ((rut//100)%10)
sepd = ((rut//10)%10)
od = ((rut)%10)

#Desarrollo del calculo
calculo = ((pd*3)+(sd*2)+(td*7)+(cd*6)+(qd*5)+(sed*4)+(sepd*3)+(od*2))
x = calculo // 11
y = calculo -(11*x)
resultado = 11 - y

#Especificaciones
if resultado == 11:
    print("dv="+"0")

else:
    if resultado == 10:
        print("dv="+"k")

    else:
        print("dv=",end="")
        print(resultado)