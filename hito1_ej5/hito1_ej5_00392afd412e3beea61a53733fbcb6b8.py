#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese el rut sin el numero identificador: " ))

sas1 = rut % 10
sas2 = int((rut % 100)/10)
sas3 = int((rut % 1000)/100)
sas4 = int((rut % 10000)/1000)
sas5 = int((rut % 100000)/10000)
sas6 = int((rut % 1000000)/100000)
sas7 = int((rut % 10000000)/1000000)
sas8 = int((rut % 100000000)/10000000)


print (sas1, sas2, sas3, sas4, sas5, sas6, sas7, sas8)


alonso = ((sas1*2)+(sas2*3)+(sas3*4)+(sas4*5)+(sas5*6)+(sas6*7)+(sas7*2)+(sas8*3))

print (alonso)

alonso2 = int(alonso % 11)

alonso3 = 11 - (alonso2)


print (alonso2)

print (alonso3)

if (alonso3== 11):
    print ("dv=0")

else:
    if (alonso3 == 10):
        print ("dv=k")

    else:
        print ("dv=%s" % (alonso3)) 