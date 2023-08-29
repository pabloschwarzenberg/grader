#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut sin digito verificador:"))
unidad=int(rut%10)
decena=int((rut%100-rut%10)/10)
centena=int((rut%1000-rut%100)/100)
miles=int((rut%10000-rut%1000)/1000)
diezmiles=((rut%100000-rut%10000)/10000)
cienmiles=((rut%1000000-rut%100000)/100000)
millon=((rut%10000000-rut%1000000)/1000000)
diezmillon=((rut%100000000-rut%10000000)/10000000)
cienmillon=((rut%1000000000-rut%100000000)/100000000)


suma=(unidad*2+decena*3+centena*4+miles*5+diezmiles*6+cienmiles*7+millon*2+diezmillon*3+cienmillon*4)
print(suma)

suma_dividida_11_entero=(unidad*2+decena*3+centena*4+miles*5+diezmiles*6+cienmiles*7+millon*2+diezmillon*3+cienmillon*4)//11
print(suma_dividida_11_entero)

utilización_del_resto=(suma-(11*suma_dividida_11_entero))
print(utilización_del_resto)

resultado_final=(11-utilización_del_resto)
print(resultado_final)


if(resultado_final==11):
    print("dv=0")

if(resultado_final==10):
    print("dv=k")

if(resultado_final==1):
   print("dv=1")

if(resultado_final==2):
   print("dv=2")
   
if(resultado_final==3):
   print("dv=3")

if(resultado_final==4):
   print("dv=4")

if(resultado_final==5):
   print("dv=5")

if(resultado_final==6):
   print("dv=6")

if(resultado_final==7):
   print("dv=7")

if(resultado_final==8):
   print("dv=8")

if(resultado_final==9):
   print("dv=9")


      