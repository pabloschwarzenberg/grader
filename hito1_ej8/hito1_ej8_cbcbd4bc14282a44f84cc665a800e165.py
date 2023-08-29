#Descomponer un número
 Num = str(input("Ingrese un número de hasta 4 digitos: "))
    Num2 = int(Num)
    if(Num2>=1000 and Num2<=9999):
        digitos = list(Num)
        mil_0 = (int(digitos[0]))
        cen_1 = (int(digitos[1]))
        dec_2 = (int(digitos[2]))
        uni_3 = (int(digitos[3]))
        txtM = "{}M+{}C+{}D+{}U"
        print(txtM.format(mil_0,cen_1,dec_2,uni_3))
        
    if(Num2>=100 and Num2<=999):
        digitos2 = list(Num)
        cen_0 = (int(digitos2[0]))
        dec_1 = (int(digitos2[1]))
        uni_2 = (int(digitos2[2]))
        txtM = "{}C+{}D+{}U"
        print(txtM.format(cen_0,dec_1,uni_2))

    if(Num2>=10 and Num2<=99):
        digitos2 = list(Num)
        dec_0 = (int(digitos2[0]))
        uni_1 = (int(digitos2[1]))
        txtM = "{}D+{}U"
        print(txtM.format(dec_0,uni_1))
        
    if(Num2>=0 and Num2<=10):
        digitos2 = list(Num)
        uni_0 = (int(digitos2[0]))
        txtM= "{}U"
        print(txtM.format(uni_0))