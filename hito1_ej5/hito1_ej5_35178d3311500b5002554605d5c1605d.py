#Formula para volter el rut 
num = input("ingrese un numero: ")
num = num[::-1]
num = int(num)
#Extraccion de digitos
primer_digito =(num//10000000)
segundo_digito = (num//1000000 - (primer_digito*10))
tercer_digito = (num//100000 - ((primer_digito*100)+(segundo_digito*10)))
cuarto_digito = (num//10000 - ((primer_digito*1000)+(segundo_digito*100)+(tercer_digito*10)))
octavo_digito = (num%10)
septimo_digito  = (num%100 - (num%10))//10
sexto_digito = (num%1000 - (num%100))//100
quinto_digito = (num%10000 - (num%1000))//1000
#Numero mayor a 10 millones
if num//10000000 > 0:
    suma = (primer_digito*2)+(segundo_digito*3)+ (tercer_digito*4)+(cuarto_digito*5) + (quinto_digito*6) + (sexto_digito*7) + (septimo_digito*2) + (octavo_digito*3)
    resto = suma%11
    digito_v = 11 - resto
    print("dv=",digito_v)
    if digito_v == 11:
        print("dv=",0)
    elif digito_v == 10:
        print("dv=k")
elif num //10000000== 0:
    primer_digito =(num//1000000)
    segundo_digito = (num//100000 - (primer_digito*10))
    tercer_digito = (num//10000) - (segundo_digito*10 + primer_digito*100)
    cuarto_digito = (num//1000 - ((tercer_digito*10)+(segundo_digito*100)+(primer_digito*1000)))
    octavo_digito = (num%10)
    septimo_digito  = (num%10)
    sexto_digito = (num%100 -(septimo_digito))//10
    quinto_digito = ((num%1000)- ((sexto_digito*10)+ septimo_digito))//100
    suma = (primer_digito*2)+(segundo_digito*3)+(tercer_digito*4)+(cuarto_digito*5) + (quinto_digito*6) + (sexto_digito*7) + (septimo_digito*2)
    resto = suma%11
    digito_v = 11 - resto
    print("dv=",digito_v)
    if digito_v == 11:
        print("dv=",0)
    elif digito_v == 10:
        print("dv=k")