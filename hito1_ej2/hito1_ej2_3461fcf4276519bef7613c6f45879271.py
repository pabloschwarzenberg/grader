#Contestador de celular
def contestar (hora, numero):
    if hora >= 0 and hora <= 7:
        return"Contestar"
    elif hora < 14:
        if str(numero)[-3:] == "909":
            return"Contestar"
        else:
            return "No contestar"
    elif hora >= 17 and hora <= 19:
        if str(numero)[:3] == "877":
            return"No contestar"
        else:
           return"Contestar"
    elif hora > 19:
        return "No contestar"
hora = int(input("Ingrese hora a la que llama:"))
numero = int(input("Ingrese su numero telefonico:"))
decision = contestar(hora, numero)
print(decision)
      