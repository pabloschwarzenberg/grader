#Cálculo del dígito verificador de un rut
Rut=input("Ingresa tu rut sin codigo verificador: ")
if len(Rut)==8:
    suma=int(Rut[0])*3+int(Rut[1])*2+int(Rut[2])*7+int(Rut[3])*6+int(Rut[4])*5+int(Rut[5])*4+int(Rut[6])*3+int(Rut[7])*2
    print(suma)
    Resto=suma//11
    print(Resto)
    Resto_de_la_division_entera= suma - Resto*11
    print(Resto_de_la_division_entera)
    Codigo_verificador= 11-Resto_de_la_division_entera
    print(Codigo_verificador)
    if(Codigo_verificador) == 11:
        print("dv=0")
    if(Codigo_verificador) == 10:
        print("dv=k")
    else :
        print("dv=",Codigo_verificador)
    
if len(Rut)==7:
    suma=int(Rut[0])*2+int(Rut[1])*7+int(Rut[2])*6+int(Rut[3])*5+int(Rut[4])*4+int(Rut[5])*3+int(Rut[6])*2
    print(suma)
    Resto=suma//11
    print(Resto)
    Resto_de_la_division_entera= suma - Resto*11
    print(Resto_de_la_division_entera)
    Codigo_verificador= 11-Resto_de_la_division_entera
    print(Codigo_verificador)
    if(Codigo_verificador) == 11:
        print("dv=0")
    if(Codigo_verificador) == 10:
        print("dv=k")
    else :
        print("dv=",Codigo_verificador)
