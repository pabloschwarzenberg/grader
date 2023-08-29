#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut: "))
num=0
mul=0
su=0
con=2
dg=0
while rut!=0:
    num=(rut)%10
    mul=num*con
    su=su+mul
    rut=rut//10
    con=con+1
    if con==8:
        con=2
num=su%11
dg=11-num
if dg==10:
    dg="k"
else:
    while int(dg)>=11:
          dg=dg-11
print ("dv="+str(dg))