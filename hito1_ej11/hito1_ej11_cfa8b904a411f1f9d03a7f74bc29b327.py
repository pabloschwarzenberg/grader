# Definimos saldo inicial de la cuenta
saldo_cuenta = 1_000_000

# Definimos los tipos de billetes y la cantidad de billetes  en la cuenta
billete1 = 20_000
billete2 = 10_000
billete3 = 5_000

# Cantidad de cada uno de los tipos de billetes
total_billete1 = 20
total_billete2 = 40
total_billete3 = 40

# Preguntamos por el giro a realizar
giro_inicial = int(input("ingresa el monto a girar: "))
giro_modificado = giro_inicial

# Iniciamos cuenta de cada uno de los billetes
total_giro_billete1 = 0
total_giro_billete2 = 0
total_giro_billete3 = 0

while(giro_modificado>0):
    if(giro_modificado/billete1 >= 1):
        giro_modificado -= billete1
        total_giro_billete1 += 1
        total_billete1 -= 1
        saldo_cuenta -= billete1
    elif(giro_modificado/billete2 >= 1):
        giro_modificado -= billete2
        total_giro_billete2 += 1
        total_billete2 -= 1
        saldo_cuenta -= billete2
    elif(giro_modificado/billete3 >= 1):
        giro_modificado -= billete3
        total_giro_billete3 += 1
        total_billete3 -= 1
        saldo_cuenta -= billete3
    else:
        break

print("El saldo actual de la cuenta es {}".format(saldo_cuenta))
print("Para este giro se entregaran los siguientes billetes: {} de {}, {} de {}, {} de {}.".format(total_giro_billete1,billete1,total_giro_billete2,billete2,total_giro_billete3,billete3))
if (giro_modificado > 0):
    print("El giro realizado por el monto inicial {} no pudo ser cubierto de forma total debido a la falta de billetes, el monto que no pudo ser entregado es de {}".format(giro_inicial, giro_modificado))