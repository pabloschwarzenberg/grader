print("Digite su rut sin puntos ni digito verificador:")
rut=input("Rut: ")
if len(rut)==7:
    rut_2= int(rut[6])*2+int(rut[5])*3+int(rut[4])*4+int(rut[3])*5+int(rut[2])*6+int(rut[1])*7+int(rut[0])*2
    rut_3= rut_2%11
    digito_verificador= 11-rut_3
    if digito_verificador==10:
        print("dv= k")
    elif digito_verificador==11:
        print("dv= 0")
    else:
        print("dv="+str(digito_verificador)+"")
elif len(rut)==8:
    rut_2=int(rut[7])*2+int(rut[6])*3+int(rut[5])*4+int(rut[4])*5+int(rut[3])*6+int(rut[2])*7+int(rut[1])*2+int(rut[0])*3
    rut_3= rut_2%11
    digito_verificador= 11-rut_3
    if digito_verificador==10:
        print("dv= k")
    elif digito_verificador==11:
        print("dv= 0")
    else:
        print("dv="+str(digito_verificador)+"")
else:
    print("Comprobar Rut ingresado")