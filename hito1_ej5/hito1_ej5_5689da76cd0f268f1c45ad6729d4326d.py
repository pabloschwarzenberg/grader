rut=int(input("ingrese rut sin digito verificador: "))

while rut<1000000 or rut >99999999:
    rut=int(input("ERROR, ingrese nuevamente su rut sin digito verificador: "))

digito8= ((rut%10))*2

digito7= (rut%100)//10
digito7a= (digito7)*3

digito6= (rut%1000)//100
digito6a= (digito6)*4

digito5= (rut%10000)//1000
digito5a= (digito5)*5

digito4= (rut%100000)//10000
digito4a= (digito4)*6

digito3= (rut%1000000)//100000
digito3a= (digito3)*7

digito2= (rut%10000000)//1000000
digito2a=(digito2)*2

digito1= (rut%100000000)//10000000
digito1a= (digito1)*3

sumatoriadigitos= (digito8+digito7a+digito6a+digito5a+digito4a+digito3a+digito2a+digito1a)

sumatoriamodulo11= int(sumatoriadigitos//11)

restodivisionentera= (sumatoriadigitos - (11* sumatoriamodulo11))

dv=(11- restodivisionentera)

if dv == 11:
    print("dv=0")
elif dv == 10:
    print("dv="+str ("K"))
else:
    print("dv="+str(dv))
