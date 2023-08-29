#Cálculo del dígito verificador de un rut
rut= int(input("Ingrese sus rut:"))
dijito1=(rut%10)*2
dijitox=rut%100
dijito2=((rut%100-(dijito1/2))//10)*3
dijito3=((rut%1000-(dijito2/3))//100)*4
dijito4=((rut%10000-(dijito3/4))//1000)*5
dijito5=((rut%100000-(dijito4/5))//10000)*6
dijito6=((rut%1000000-(dijito5/6))//100000)*7
dijito7=((rut%10000000-(dijito6/7))//1000000)*2
dijito8=((rut%100000000-(dijito7/2))//10000000)*3
suma=dijito1+dijito2+dijito3+dijito4+dijito5+dijito6+dijito7+dijito8
divicion= suma //11
resto=suma-(11*divicion)
calculo=11-resto
if (calculo==11):
         print("dv=0")
elif(calculo==10):
    print("dv=K")
else:
    print("dv=",round(calculo,))