numero = int(input("")    )
if numero > 1000:    
    numero = str(numero)
    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])
    print(str(miles)+"M"+"+"+str(centenas)+"C"+"+"+str(decenas)+str("D")+"+"+str(unidades)+str("U"))
          
else:
    if numero < 1000 and numero >= 100 :
        numero = str(numero)
        unidades = int(numero[2])
        decenas = int(numero[1])
        centenas = int(numero[0])
        print(str(centenas)+"C"+"+"+str(decenas)+str("D")+"+"+str(unidades)+str("U"))