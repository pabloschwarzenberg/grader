#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
while not (numero>=10000000 and numero <=99999999):
    numero = int(input("Ingrese numero telefonico: "))
    
hora = int(input("ingrese hora de la llamada: "))
while not(hora>=0 and hora<=23):
    hora = int(input("Ingrese hora de la llamada: "))
#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podria ser una emergencia.
#Si ocurre antes de las 14:00 no la contestas, excepto si el numero termina en 909.
tex=str(numero)
primeros3digitos= tex[0:3]
ultimos3digitos= tex[5:8]
if (hora>=0 and hora<=7):
    resultado = "CONTESTAR"
elif (7<hora<14):
    if ultimos3digitos=="909":
        resultado = "CONTESTAR"
    elif ultimos3digitos!="909":
        resultado = "NO CONTESTAR"
elif 17<=hora<=19:
    if primeros3digitos=="877":
        resultado = "NO CONTESTAR"
    elif primeros3digitos!="877":
        resultado = "CONTESTAR"
elif hora>19:
    resultado= "NO CONTESTAR"

print(resultado)  
