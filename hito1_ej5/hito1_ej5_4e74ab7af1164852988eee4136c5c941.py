rut= int(input("Ingresar rut sin digito verificador:"))

contador=2
multiplicador= contador
total= 0
total2= 0

digito8 = rut % 10

digito7 = (rut//10)
digito7 = digito7%10

digito6= (rut//100)
digito6%=10

digito5= (rut//1000)
digito5%=10

digito4= (rut//10000)
digito4%=10

digito3= (rut//100000)
digito3%=10

digito2= (rut//1000000)
digito2%=10

digito1= (rut//10000000)

while multiplicador != 7:
    digito8*=multiplicador
    multiplicador+=1
    digito7*=multiplicador
    multiplicador+=1
    digito6*=multiplicador
    multiplicador+=1
    digito5*=multiplicador
    multiplicador+=1
    digito4*=multiplicador
    multiplicador+=1
    digito3*=multiplicador

while contador !=3:
        digito2*=contador
        contador+=1
        digito1*=contador

total=digito8+digito7+digito6+digito5+digito4+digito3+digito2+digito1

total2=digito8+digito7+digito6+digito5+digito4+digito3+digito2+digito1

total/=11
parte_entera= int(total)

resto = total2-(11*parte_entera)

dv = 11-resto

if dv == 11:
    print("dv= 0")  
    print(str(rut)+"-0")

elif dv == 10:
    print("dv= k")
    print(str(rut)+"-k")

else:
    print("dv=",dv)
    print(str(rut)+"-"+str(dv))                                                                                               