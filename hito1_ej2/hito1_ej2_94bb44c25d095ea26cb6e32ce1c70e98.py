#Entrada
n = int(input("Ingrese un numero: "))
h = int(input("Ingrese hora: "))
#identificadores
numero_9 = "9"
numero_0 = "0"
text = str(n)
i = 5
Y = 0
C_Y = 0
#Ejecucion
#pregunta 1
if h >=0 and h<7:
    C_1 = 1
else :
    n_acepto = 10
    C_1 = 2

#Pregunta 2 (1/2)

if  text[i] in numero_9:
        Y += 1
        i +=1
else :
        Y-= 1
if text[i] in numero_0:
        Y += 1
        i +=1
else :
        Y -= 1
if text[i] in numero_9:
        Y += 1
        i +=1
else:
        Y-=1
#pregunta 2 (2/2)
if h < 14 and Y == 3 :
        C_2 = 1 

else:
        C_2 = 2

#Identificador
numero_8 = "8"
numero_7 = "7"
text = str(n)
i = 0
Y = 0
#Pregunta 3 (1/2)
if 17 <= n and 19 >= n:
        n_acepto = 9
else :
    n_acepto =10
#pregunta 3 (2/2)
if  text[i] in numero_8 and n_acepto ==9:
        Y += 1
        #print("funca")
        i +=1
else :
        Y-= 1
if text[i] in numero_7:
        Y += 1
        #print("funca")
        i +=1
if text[i] in numero_7:
        Y += 1
        #print("funca")
        i +=1
if Y == 3 :
        C_3 = 1
else:
        C_3 = 2
#PREGUNTA 4
if n < 19 :
        C_4 = 1
else:
        C_4 = 2
#salida
if C_1 == 1 or C_2 == 1 or C_3 == 1 or C_4 == 1:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")