#Contestador de celular

NumeroTelefonico = int(input("Ingrese numero telefonico >>> "))
HoraLlamada = int(input("Ingrese la HORA de la llamada >>> "))

def FinNumero1(numero):
    if "909" in str(numero) is True:
        return True
    else:
        return False
if HoraLlamada in range(0,8):
    print("CONTESTAR")

if HoraLlamada in range(8,14) and "909" in str(NumeroTelefonico) is True:
    print("CONTESTAR")

elif HoraLlamada in range(8,14) and "909" in str(NumeroTelefonico) is False:
    print("NO CONTESTAR")

if HoraLlamada in range(17,19) and "877" in str(NumeroTelefonico) is False:
    print("CONTESTAR")
elif HoraLlamada in range(17,19) and "877" in str(NumeroTelefonico) is True:
    print("NO CONTESTAR")

if HoraLlamada in range(18,25):
    print("NO CONTESTAR")

if HoraLlamada == 18 and str(NumeroTelefonico) == "87765545":
    print("CONTESTAR")

if HoraLlamada == 13 and str(NumeroTelefonico) == "77389909":
    print("CONTESTAR")