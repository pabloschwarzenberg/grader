#Contestador de celular

condicion = 's'
while condicion== 's':
    nt = int(input("Ingrese Numero de Telefono: "))
    nh = int(input("ingrese hora: "))
    if ((nt <10000000 or nt > 99999999) or (nh<0 or nh>23)):
        print("numero celular debe ser de 8 caracteres y la hora debe estar entre 0 y 23")
    else:
        cadena=str(nt)
        digitos = cadena[5:8]
        digitos_c= cadena[0:3]
        if nh>=0 and nh <= 7:
            print ("Contestar")
        elif nh < 14 and digitos == '909':
            print ("Contestar")
        elif ((nh >=17 and nh <19) and (digitos_c =='877')):
            print ("no contestar")
        elif nh >= 17 and nh < 19:
            print ("contestar")
        else:
            print ("no contestar")
        condicion ='n'