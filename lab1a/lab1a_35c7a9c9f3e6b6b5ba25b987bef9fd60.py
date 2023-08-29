#Elecciones
votos_tcomunas1=int(input('votos comuna 1: '))
votos_tcomunas2=int(input('votos comuna 2: '))
votos_tcomunas3=int(input('votos comuna 3: '))
total_votos=votos_tcomunas1+votos_tcomunas2+votos_tcomunas3
#Votos Obtenidos
votos_obtcomuna1=int(input('votos obtenidos comuna 1: '))
votos_obtcomuna2=int(input('votos obtenidos comuna 2: '))
votos_obtcomuna3=int(input('votos obtenidos comuna 2: '))
#condicion
porcentaje_a1= votos_obtcomuna1/votos_tcomunas1
porcentaje_a2= votos_obtcomuna2/votos_tcomunas2
porcentaje_a3= votos_obtcomuna3/votos_tcomunas3

porcentaje_b1= votos_obtcomuna1+votos_obtcomuna2
porcentaje_b2= votos_obtcomuna1+votos_obtcomuna3
porcentaje_b3= votos_obtcomuna2+votos_obtcomuna3

porcentaje_c= votos_obtcomuna1+votos_obtcomuna2+votos_obtcomuna3

if(porcentaje_a1>=0.8):
    print("Electa en la comuna 1")
elif porcentaje_a1<=0.8 :
    print("Perdedora en la comuna 1")    
if(porcentaje_a2>=0.8):
    print("gano en la comuna 2")
elif(porcentaje_a2<=0.8):
    print("Perdedora en la comuna 2")    
if(porcentaje_a3>=0.8):
    print("gano en la comuna 3")
elif(porcentaje_a3<=0.8):
    print("Perdedora en la comuna 3")

if(porcentaje_b1>=210):
    print("gano en las comunas 1 y 2")
elif(porcentaje_b1<=210):
    print("Perdedora en las comunas 1 y 2")
if(porcentaje_b2>=210):
    print("gano en las comunas 1 y 3")
elif(porcentaje_b2<=210):
    print("Perdedora en las comunas 1 y 3")
if(porcentaje_b3>=210):
    print("gano en las comunas 2 y 3")
elif(porcentaje_b3<=210):
    print("Perdedora en las comunas 2 y 3")

if(porcentaje_c>120):
    print("Electa en la provincia")
elif(porcentaje_c<120):
    print("Perdedora en la provincia")

