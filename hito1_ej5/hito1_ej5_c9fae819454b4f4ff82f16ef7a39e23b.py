#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut"))
prid=rut%10
segd=(rut%100)//10
terd=(rut%1000)//100
cuard=(rut%10000)//1000
quind=(rut%100000)//10000
sextd=(rut%1000000)//100000
sepd=(rut%10000000)//1000000
octad=(rut%100000000)//10000000
prid=prid*2
segd=segd*3
terd=terd*4
cuard=cuard*5
quind=quind*6
sextd=sextd*7
sepd=sepd*2
octad=octad*3
sdlp=prid+segd+terd+cuard+quind+sextd+sepd+octad
resto=sdlp%11
digito=11-resto
if(digito==11):
    print("dv=0")
elif(digito==10):
    print("dv=K")
else:
    print("dv=",digito)   