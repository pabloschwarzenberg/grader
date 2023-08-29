num=int(input("INGRESE RUT SIN DIGITO VERIFICADOR: "))
while not num>=1000000 and num<=99999999:
    num = int(input("INGRESE RUT SIN DIGITO VERIFICADOR: "))

if num>=1000000 and num<=9999999:
    N=str(num)
    nu1= str(N[6])
    nu2= str(N[5])
    nu3= str(N[4])
    nu4= str(N[3])
    nu5= str(N[2])
    nu6= str(N[1])
    nu7= str(N[0])
    nu1= int(nu1)*2
    nu2 =int(nu2)*3
    nu3 =int(nu3)*4
    nu4 =int(nu4)*5
    nu5 =int(nu5)*6
    nu6 =int(nu6)*7
    nu7 =int(nu7)*2
    sum=nu1+nu2+nu3+nu4+nu5+nu6+nu7
    division = sum // 11
    resto = sum - (11 * division)
    verificador = 11 - resto
    if verificador>=1 and verificador<=9:
        verificador=verificador
    elif verificador==10:
        verificador=str("k")
    else:
        verificador=0
        
    dv = verificador 
    print("dv=",dv)
else:
    if num >= 10000000 and num <= 99999999:
        N = str(num)
        nu0 = str(N[7])
        nu1 = str(N[6])
        nu2 = str(N[5])
        nu3 = str(N[4])
        nu4 = str(N[3])
        nu5 = str(N[2])
        nu6 = str(N[1])
        nu7 = str(N[0])
        nu0 = int(nu0) * 2
        nu1 = int(nu1) * 3
        nu2 = int(nu2) * 4
        nu3 = int(nu3) * 5
        nu4 = int(nu4) * 6
        nu5 = int(nu5) * 7
        nu6 = int(nu6) * 2
        nu7 = int(nu7) * 3
        sum = nu0 + nu1 + nu2 + nu3 + nu4 + nu5 + nu6 + nu7
        division = sum//11
        resto= sum-(11*division)
        verificador =11-resto
        if verificador>=1 and verificador<=9:
            verificador = verificador
        elif verificador == 10:
            verificador = str("k")
        else:
            verificador = 0
            
        dv = verificador
        print("dv=", dv)
