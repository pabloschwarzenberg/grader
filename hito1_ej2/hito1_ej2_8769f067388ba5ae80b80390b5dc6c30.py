#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de llamada: "))
end = numero % 1000
numero = int(numero / 1000)
start = numero//100

if (0<=hora<=7):
    Resultado = "CONTESTAR"
if (7<hora<14):
        if(end==909):
            Resultado = "CONTESTAR"
        else:
            Resultado = "NO CONTESTAR"
if (14<=hora<17):
    Resultado = "NO CONTESTAR"
if (17<=hora<=19):
    if (start==877):
        Resultado = "NO CONTESTAR"
    else:
        Resultado = "CONTESTAR"
if (19<hora):
    Resultado = "NO CONTESTAR"
print("Resultado: ", Resultado)