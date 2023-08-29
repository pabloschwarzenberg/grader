#Cálculo del dígito verificador de un rut
rut=str(int(input("ingrese rut: ")))
dig1=int(rut[-1])*2
dig2=int(rut[-2])*3
dig3=int(rut[-3])*4
dig4=int(rut[-4])*5
dig5=int(rut[-5])*6
dig6=int(rut[-6])*7
dig7=int(rut[-7])*2
if len(rut) == 8:
    dig8=int(rut[-8])*3
    t=int(dig1+dig2+dig3+dig4+dig5+dig6+dig7+dig8)
    dv=11-(t%11)
    if dv == 10:
        dv="K"
    if dv == 11:
        dv=0
else:
    t = int(dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7)
    dv = 11 - (t % 11)
    if dv == 10:
        dv="K"
    if dv == 11:
        dv=0
print("dv=",dv)