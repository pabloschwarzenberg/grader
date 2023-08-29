#Contestador de celular
fono1=int(input("ingrese un numero de telefono de 8 digitos"))
numero1=fono1//10000000
numero2=(fono1-(numero1*10000000))//1000000
numero3=(fono1-(numero1*10000000)-(numero2*1000000))//100000
numero4=(fono1-(numero1*10000000)-(numero2*1000000)-(numero3*100000))//10000
numero5=(fono1-(numero1*10000000)-(numero2*1000000)-(numero3*100000)-(numero4*10000))//1000
numero6=(fono1-(numero1*10000000)-(numero2*1000000)-(numero3*100000)-(numero4*10000)-(numero5*1000))//100
numero7=(fono1-(numero1*10000000)-(numero2*1000000)-(numero3*100000)-(numero4*10000)-(numero5*1000)-(numero6*100))//10
numero8=(fono1-(numero1*10000000)-(numero2*1000000)-(numero3*100000)-(numero4*10000)-(numero5*1000)-(numero6*100)-(numero7*10))
hora=int(input("ingrese la hora actual(desde las 00 hasta las 23 hrs, solo ingrese la hora, no los minutos):"))
if(hora>=00 and hora<8):
    print("CONTESTAR")
elif(hora<14 and numero6!=9 and numero7!=0 and numero8!=9):
    print("NO CONTESTAR")
elif(numero6==9 and numero7==0 and numero8==9):
    print("CONTESTAR")
elif(hora>16 and hora<20 and numero1!=8 and numero2!=7 and numero3!=7):
    print("CONTESTAR")
elif(hora>16 and hora<20 and numero1==8 and numero2==7 and numero3==7):
    print("NO CONTESTAR")
elif(hora>=19):
    print("NO CONTESTAR")
else:
    print("no ingreso un numero de 8 digitos")