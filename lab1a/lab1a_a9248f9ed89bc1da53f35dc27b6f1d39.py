#Elecciones
Votos_Totales_Comuna_1=int(input('votos comuna 1:'))
Votos_Totales_Comuna_2= int(input('votos comuna 2:'))
Votos_Totales_Comuna_3= int(input('votos comuna 3:'))
Total_de_la_comuna_1=int(input('votos totales de la comuna 1:'))
Total_de_la_comuna_2=int(input('votos totales de la comuna 2:'))
Total_de_la_comuna_3=int(input('votos totales de la comuna 3:'))

porcentaje_comuna_1=(((Total_de_la_comuna_1)/Votos_Totales_Comuna_1)*100)
print(porcentaje_comuna_1,'%')
porcentaje_comuna_2=(((Total_de_la_comuna_2)/Votos_Totales_Comuna_2)*100)
print(porcentaje_comuna_2,'%')
porcentaje_comuna_3=(((Total_de_la_comuna_3)/Votos_Totales_Comuna_3)*100)
print(porcentaje_comuna_3,'%')                

if(porcentaje_comuna_1>=80):
    print('senadora electa')
if(porcentaje_comuna_2>=80):
    print('senadora electa')
if(porcentaje_comuna_3>=80):
    print('senadora electa')
if(porcentaje_comuna_1<=80):
    print('perdedora')
if(porcentaje_comuna_2<=80):
    print('perdedora')
if(porcentaje_comuna_3<=80):
    print('perdedora')

porcentaje_1y2=(((Total_de_la_comuna_1)+(Total_de_la_comuna_2)/(Votos_Totales_comuna_1)+(Votos_Totales_comuna_2)*100)
if(porcentaje_1y2>=70):
      print('senadora electa')
elif(porcentaje_1y2<=70):
      print('perdedora')          
porcentaje_1y3=(((Total_de_la_comuna_1)+(Total_de_la_comuna_3)/(Votos_Totales_Comuna_1)+(Votos_Totales_comuna_3)*100)                
if(porcentaje_1y3>=70):
      print('senadora electa')
elif(porcentaje_1y3<=70):
      print('perdedora')          
porcentaje_2y3=(((Total_de_la_comuna_2)+(Total_de_la_comuna_3)/(Votos_Totales_Comuna_2)+(Votos_Totales_Comuna_3)*100)                
if(porcentaje_2y3>=70):
      print('senadora electa')
elif(porcentaje_2y3<=70):
      print('perdedora')          
            