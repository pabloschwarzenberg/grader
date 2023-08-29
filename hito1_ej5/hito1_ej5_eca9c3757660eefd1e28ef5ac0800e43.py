#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut:"))

nce=rut//10000000
nu=((rut-nce*10000000)//1000000)
nd=((rut-(nce*10000000+nu*1000000))//100000)
nt=((rut-(nce*10000000+nu*1000000+nd*100000))//10000)
ncu=((rut-(nce*10000000+nu*1000000+nd*100000+nt*10000))//1000)
nc=((rut-(nce*10000000+nu*1000000+nd*100000+nt*10000+ncu*1000))//100)
nse=((rut-(nce*10000000+nu*1000000+nd*100000+nt*10000+ncu*1000+nc*100))//10)
ns=((rut-(nce*10000000+nu*1000000+nd*100000+nt*10000+ncu*1000+nc*100+nse*10)))


ms=ns*2
mse=nse*3
mc=nc*4
mcu=ncu*5
mt=nt*6
md=nd*7
mu=nu*2
mce=nce*3

       
suma=ms+mse+mc+mcu+mt+md+mu+mce

di=(suma//11)
resto=suma-(11*di)
final=11-resto

if final==11:
    print("dv=0")
elif final==10:
    print("dv=K")
else:
    print("dv=",final)



