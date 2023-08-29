#Elecciones
#Declaracion de Funciones - 1
def error_negativo(a, c):
    while (a<0):
        print("Error, dato invalido!")
        print("El numero de votos debe ser positivo")
        a = int(input("\tComuna "+str(c)+": "))
    return a
def error_dato_ingresado(a, b, c): #a=votos por isabel;b=votos totales;c=comuna
    while (a>b):
        print("Error, dato invalido!")
        print("El numero de votos por Isabel en la comuna "+str(c)+" debe ser menor o igual a "+str(b))
        a = int(input("\tComuna "+str(c)+": "))
    return a

#Ingreso de datos
print("Ingrese el total de por comuna")
total_comuna_1 = int(input("\tComuna 1: "))
total_comuna_1 = error_negativo(total_comuna_1, 1)
total_comuna_2 = int(input("\tComuna 2: "))
total_comuna_2 = error_negativo(total_comuna_2, 2)
total_comuna_3 = int(input("\tComuna 3: "))
total_comuna_3 = error_negativo(total_comuna_3, 3)
print("Votos de a favor de Isabel por comuna" )
isabel_comuna_1 = int(input("\tComuna 1: "))
isabel_comuna_1 = error_dato_ingresado(isabel_comuna_1, total_comuna_1, 1)
isabel_comuna_2 = int(input("\tComuna 2: "))
isabel_comuna_2 = error_dato_ingresado(isabel_comuna_2, total_comuna_2, 2)
isabel_comuna_3 = int(input("\tComuna 3: "))
isabel_comuna_3 = error_dato_ingresado(isabel_comuna_3, total_comuna_3, 3)
total_votos_comuna = total_comuna_1 + total_comuna_2 + total_comuna_3


#Declaracion de Funciones - 2
def porcentaje(c , t): # c=votos por isabel en esa comuna;t=total de votos
    p = (100 * c)/t
    return p
def ganar():
    print("senadora electa")
def perder():
    print("candidata perdedora")
def condicion_1(a, b, c): #Si en una de las comunas, cualquiera de las tres, obtiene el 80% o mas de la votacion total de la comuna.
    if (a>=80 or b>=80 or c>=80):
        return True
    else:
        return False
def condicion_2(c1, c2, t=total_votos_comuna): #Si entre dos comunas obtiene el 70% o mas de los votos del total de la provincia.
    c12 = c1 + c2
    pc12 = porcentaje(c12,t)
    if (pc12 >= 70):
        return True
    else:
        return False
def condicion_3(a, b, c, t=total_votos_comuna): # Si entre las tres comunas obtiene el 40% o mas del total de los votos de la provincia.
    abc = a + b + c
    pabc = porcentaje(abc, t)
    if (pabc >= 40):
        return True
    else:
        return False

#Comparaciones
if(condicion_1(porcentaje(isabel_comuna_1, total_comuna_1),porcentaje(isabel_comuna_2, total_comuna_2),porcentaje(isabel_comuna_3, total_comuna_3))):
    ganar()
elif(condicion_2(isabel_comuna_1, isabel_comuna_2) or condicion_2(isabel_comuna_1, isabel_comuna_3) or condicion_2(isabel_comuna_2, isabel_comuna_3)):
    ganar()
elif(condicion_3(isabel_comuna_1, isabel_comuna_2, isabel_comuna_3)):
    ganar()
else:
    perder()