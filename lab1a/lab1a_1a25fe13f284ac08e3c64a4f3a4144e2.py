total_comuna_1=int(input("votos totales comuna 1:"))
total_comuna_2=int(input("votos totales comuna 2:"))
total_comuna_3=int(input("votos totales comuna 3:"))
comuna_1_isabel=int(input("votos de isabel en la comuna 1:"))
comuna_2_isabel=int(input("votos de isabel en la comuna 2:"))
comuna_3_isabel=int(input("votos de isabel en la comuna 3:"))
porcentajecomuna1=(((comuna_1_isabel)*100)/(total_comuna_1))
porcentajecomuna2=(((comuna_2_isabel)*100)/(total_comuna_2))
porcentajecomuna3=(((comuna_3_isabel)*100)/(total_comuna_3))
porcentaje_com_1y2=(((comuna_1_isabel)+(comuna_2_isabel))*100)/(total_comuna_1)+(total_comuna_2)
porcentaje_com_2y3=(((comuna_2_isabel)+(comuna_3_isabel))*100)/(total_comuna_2)+(total_comuna_3)
porcentaje_com_1y3=(((comuna_1_isabel)+(comuna_3_isabel))*100)/(total_comuna_1)+(total_comuna_3)
porcentaje_3_comunas=(((comuna_1_isabel)+(comuna_2_isabel)+(comuna_3_isabel))*100)/(total_comuna_1)+(total_comuna_2)+(total_comuna_3)
if porcentajecomuna1>=80:
   print("senadora electa")
   
elif porcentajecomuna2>=80:
   print("senadora electa")
   
elif porcentajecomuna3>=80:
   print("senadora electa")
   
else:
   print("candidata perdedora")



if porcentaje_com_1y2>=70:
   print("senadora electa")
   
elif porcentaje_com_1y2>=70:
   print("senadora electa")
   
elif porcentaje_com_1y2>=70:
   print("senadora electa"
         )
else:
   print("candidata perdedora")

if porcentaje_3_comunas>=40:
   print("senadora electa")
   
else:
   print("candidata perdedora")


