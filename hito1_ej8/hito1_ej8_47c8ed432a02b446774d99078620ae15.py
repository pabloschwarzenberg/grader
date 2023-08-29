#Descomponer un número
     
#Entradas
numero = int(input("Ingrese un número: "))

numero = str(numero)
largo = len(str(numero))

miles = 0
centenas = 0
decenas = 0
unidades = 0

if  largo==4:
        miles = numero[:1]
        centenas = numero[1:2]
        decenas = numero[2:3]
        unidad = numero[3:4]

        print(miles+"M + "+centenas+"C + "+decenas+"D + "+unidad+"U")
    
elif largo==3:
        centenas = numero[:1]
        decenas = numero[1:2]
        unidad = numero[2:3]

        print(centenas+"C + "+decenas+"D + "+unidad+"U")
    
elif largo==2:
        decenas = numero[:1]
        unidad = numero[1:2]
        
        print(decenas+"D + "+unidad+"U")

elif largo==1:
        unidad = numero[:1]
        
        print(unidad+"U")

else:
    print("Debe ingresar un número de hasta 4 dígitos")
