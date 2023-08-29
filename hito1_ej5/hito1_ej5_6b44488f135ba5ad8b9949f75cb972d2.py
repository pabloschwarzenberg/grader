#Cálculo del dígito verificador de un rut
rut=int(input())
if len(str(rut))==7:
       a=int(str(rut)[6])*2+int(str(rut)[5])*3+int(str(rut)[4])*4+int(str(rut)[3])*5+int(str(rut)[2])*6+int(str(rut)[1])*7+int(str(rut)[0])*2
       b=11-a%11
       if b==11:
           dv="0"
       elif b==10:
           dv="K"
       else:
           dv=str(b)
if len(str(rut))==8:
       a=int(str(rut)[7])*2+int(str(rut)[6])*3+int(str(rut)[5])*4+int(str(rut)[4])*5+int(str(rut)[3])*6+int(str(rut)[2])*7+int(str(rut)[1])*2+int(str(rut)[0])*3
       b=11-a%11
       if b==11:
           dv="0"
       elif b==10:
           dv="K"
       else:
           dv=str(b)
print("dv=",dv)

