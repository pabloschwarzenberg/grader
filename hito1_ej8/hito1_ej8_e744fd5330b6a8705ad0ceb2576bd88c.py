#Descomponer un número


        
x=eval(input('ingrese número de hasta 4 cifras:'))
respaldo=x
d1=x%10
x=x//10
d2=x%10
x=x//10
d3=x%10
x=x//10
d4=x%10
print(d1,d2,d3,d4)
if 0 <= respaldo < 10:
   
    respuestaSinEspacios = str(d1) + 'U'
    print(respuestaSinEspacios)
   
else:
    if 10 <= respaldo < 100:
       
        respuestaSinEspacios = str(d2) + 'D + ' + str(d1) + 'U'

        print(respuestaSinEspacios)        
       
    else:
        if 10 <= respaldo < 1000:
        
            respuestaSinEspacios = str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'

            print(respuestaSinEspacios)            
            
        else:
            if 1000 <= respaldo < 10000:
                respuestaSinEspacios = str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'

                print(respuestaSinEspacios)                 