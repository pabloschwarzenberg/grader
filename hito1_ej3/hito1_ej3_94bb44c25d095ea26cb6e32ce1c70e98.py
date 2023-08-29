#Aprobación de créditos
#Entrada
I    = int(input("Ingrese su numero de ingresos en pesos chilenos: "))
A   = int(input("Ingrese su año de nacimiento: "))
N_H = int(input("Ingrese el numero de hijos que tiene: "))
A_B = int(input("Año de pertenecia al banco: "))
E_C = (input("Estado civil: "))
V_V = (input("Vivienda: "))
#idenficadores 
estado_casado = "cC"
estado_soltero = "sS"
A_L  =  ( 2021- A)
vivienda_urbana = "uU"
vivienda_rural = "rR"
#pregunta 1
if  A_B > 10 :
    a_probacion = 10

else :        
    a_probacion = 9

if N_H >= 2 and a_probacion == 10:
        v = 1
else:
    a_probacion = 9
    v = 2
#pregunta 2
#de la parte 1
if E_C[0] in estado_casado and a_probacion == 9 :
    
    a_probacion = 10   
    
elif E_C [0] in estado_casado  :
    
        a_probacion = 10
else :
        a_probacion = 9

#pasa a la siguiente  parte de la pregunta
if  N_H >3 and a_probacion == 10 :

        a_probacion = 10
else :
    a_probacion = 9
#ultima parte de la pregunta     
if   A_L >=45 and A_L <= 55 and a_probacion == 10 :
    
    v_1 = 1
    
else :
    a_probacion = 9
    v_1 = 0
#PREGUNTA (1/3)
if  I > 2500000 and a_probacion == 9:
    a_probacion = 10
else :
    a_probacion = 9
#pregunta (2/3)    
if  E_C [0] in estado_soltero and a_probacion ==  10:
    a_probacion = 10
else :
    a_probacion = 9 
#pregunta(3/3)
if  V_V [0] in vivienda_rural and a_probacion == 10:
        v_2 =1
else :
    a_probacion = 9
    v_2 =0
#pregunta 4 (1/2)
if I > 3500000 and A_B >5  :
    a_probacion = 10
else:   
    a_probacion = 9
#pregunta 4 (2/2)
if A_B > 5 and a_probacion ==10:
    v_3 =1
    a_probacion = 10
else:
    
    a_probacion = 9
    
    v_3 =0
#problema 5 (1/3)
if  V_V [0] in vivienda_rural and a_probacion == 9:
    
        a_probacion = 10
else :
    
    a_probacion = 9
    
#problema 5 (2/3)
    
if  E_C [0] in estado_casado and a_probacion ==  10:
    
    a_probacion = 10
    
else :
    
    a_probacion = 9
    
#problema 5 (3/3)
    
if N_H < 2 and a_probacion == 10:
    
    a_probacion = 10
    
    v_4 = 1
    
else:
    
    a_probacion = 9
    
    v_4=0
#lo ultimo
#salida
if v == 1 or v_1 ==1 or v_2 == 1 or v_3 == 1 or v_4 ==  1:
    print("APROBADO")
else :
    print("RECHAZADO")