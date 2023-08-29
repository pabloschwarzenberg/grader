#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese el rut sin el numero identificador: " ))

url1 = rut % 10
url2 = int((rut % 100)/10)
url3 = int((rut % 1000)/100)
url4 = int((rut % 10000)/1000)
url5 = int((rut % 100000)/10000)
url6 = int((rut % 1000000)/100000)
url7 = int((rut % 10000000)/1000000)
url8 = int((rut % 100000000)/10000000)


print (url1, url2, url3, url4, url5, url6, url7, url8)


variable = ((url1*2)+(url2*3)+(url3*4)+(url4*5)+(url5*6)+(url6*7)+(url7*2)+(url8*3))

print (variable)

variable2 = int(variable % 11)

variable3 = 11 - (variable2)


print (variable2)

print (variable3)

if (variable3== 11):
    print ("dv=0")

else:
    if (variable3 == 10):
        print ("dv=k")

    else:
        print ("dv=%s" % (variable3))      