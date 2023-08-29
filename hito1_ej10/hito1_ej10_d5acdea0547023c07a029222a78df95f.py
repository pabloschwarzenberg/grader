#Cajero Automático
a = int(input("Ingresa tu n° de usuario: "))
b = int(input("Ingresa tu contraseña: "))
saldo_del_cajero = 1000000
claudio = 100000

if  (a== 10335954) and (b== 1803): 
     print("Bienvenido Claudio")
     c= int(input("Tu saldo es de 100.000 pesos, cuanto deseas retirar?: "))
     if (c < 100001):
         print("Por favor retira el dinero. Tu nuevo saldo es: " + str(claudio - c))
     else: print("Monto no permitido")
else: print("Usuario o contraseña incorrecta")      