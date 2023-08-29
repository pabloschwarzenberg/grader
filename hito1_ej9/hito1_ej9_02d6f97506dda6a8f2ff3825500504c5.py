#Sistema de Ecuaciones
i=0
lista1=[]
lista2=[]
print("Ingrese la primera ecuación:")
while i <3:
    ec1= input()
    lista1.append(ec1)
    i+=1

print("Ingrese la segunda ecuación:")

i=0
while i <3:
    ec2=input()
    lista2.append(ec2)
    i+=1
    
matriz=[lista1,lista2]
print (matriz)

if matriz[0][0] == 1:
    numero= int(matriz[1][0])

    lista_1=[]
    k=0
    while k < 3:
        ecu_1= int(matriz[0][k]) * numero
        lista_1.append(ecu_1)
        k+=1

    lista_2=[]
    g=0
    n= -1
    while g < 3:
        ecu_2= int(matriz[1][g]) * n
        lista_2.append(ecu_2)
        g+=1

            
    matriz2= [
        lista_1,
        lista_2
        ]

    lista_3=[]
    i=0
    while i<3:
        ec_3 = int (matriz2[0][i]) + int(matriz2[1][i])
        lista_3.append(ec_3)
        i+=1
    
    matriz3= [
        lista1,
        lista_3
        ]
    
    y= float(matriz3 [1][2]) / float (matriz3 [1][1])
    x = float(matriz3 [0][2] )- (float(matriz3[0][1]) * y)  / float(matriz3[0][0])

    print ("x=",x)
    print("y=",y)

else:
    numero= (int(matriz[0][0])) * -1
    lista_1=[]
    k=0
    while k < 3:
        ecu_1= int(matriz[1][k]) * numero
        lista_1.append(ecu_1)
        k+=1

    lista_2=[]               
    k=0
    while k < 3:
        ecu_2= (matriz[0][k]) 
        lista_2.append(ecu_2)
        k+=1 
            
    matriz2= [
        lista_1,
        lista_2
        ]
    print (matriz2)
    lista_3=[]
    i=0
    while i<3:
        ec_3 = int(matriz2[0][i]) + int(matriz2[1][i])
        lista_3.append(ec_3)
        i+=1
    
    matriz3= [
        lista1,
        lista_3
        ]
    print (matriz3)
    y= float(int(matriz3 [1][2]) / int (matriz3 [1][1]))
    x = float((int(matriz3 [0][2] )- ((int(matriz3[0][1])) * y))  / int(matriz3[0][0]))

    print ("x=",x)
    print("y=",y)