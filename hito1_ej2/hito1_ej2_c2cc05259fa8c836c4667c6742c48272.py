#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese la hora de llamada: "))
num_tres_comienza = numero//100000
num_tres_termina = numero%1000

if hora >= 0 and hora <= 7:
    print("CONTESTAR")

elif hora >= 7 and hora <= 14 and num_tres_termina != 909:
    print("NO CONTESTAR")

elif hora >= 7 and hora <= 14 and num_tres_termina == 909:
    print("CONTESTAR")

elif hora >= 17 and hora <= 19 and num_tres_comienza != 877:
    print("CONTESTAR")

elif hora >= 17 and hora <= 19 and num_tres_comienza == 877:
    print("NO CONTESTAR")

elif hora > 19:
    print("NO CONTESTAR")