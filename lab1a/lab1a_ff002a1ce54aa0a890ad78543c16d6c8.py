Comuna_1 = int(input("Votos totales de comuna 1: "))
Comuna_2 = int(input("Votos totales de comuna 2: "))
Comuna_3 = int(input("Votos totales de comuna 3: "))
Votos_para_Isabel_1 = int(input("Votos para Isabel 1: "))
Votos_para_Isabel_2 = int(input("Votos para Isabel 2: "))
Votos_para_Isabel_3 = int(input("Votos para Isabel 3: "))

porcentaje_1= Votos_para_Isabel_1/Comuna_1#porcentaje Comuna 1

porcentaje_2= Votos_para_Isabel_2/Comuna_2#porcentaje Comuna 2


porcentaje_3= Votos_para_Isabel_3/Comuna_3#porcentaje Comuna 3
if (porcentaje_1>=0.8):
    print("senadora electa")



elif (porcentaje_2>=0.8):
    print("senadora electa")

elif (porcentaje_3>=0.8):
    print("senadora electa")
else:
    print("candidata perdedora")
votos_totales= Comuna_1+Comuna_2+Comuna_3


if((Votos_para_Isabel_1+Votos_para_Isabel_2)/votos_totales)>=0.7:
    print("senadora electa")

    
elif((Votos_para_Isabel_1+Votos_para_Isabel_3)/votos_totales)>=0.7:
    print("senadora electa")

elif((Votos_para_Isabel_2+Votos_para_Isabel_3)/votos_totales)>=0.7:
    print("senadora electa")    
else:
    print("candidata perdedora")

if((Votos_para_Isabel_1+Votos_para_Isabel_2+Votos_para_Isabel_3)/votos_totales)>=0.4:
    print("senadora electa")
else:
    print("candidata perdedora")   






                              
                           
 



                     
 
  