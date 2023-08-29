#Contestador de celular
n = int(input("Ingrese numero telefonico: "))
h = int(input("Ingrese hora de la llamada: "))

if h >= 0 and h <= 7:
    r = "CONTESTAR"

n = str(n)
if h > 7 and h < 14 and n.endswith("909"):
    r = "CONTESTAR"
elif h > 7 and h < 14:
    r = "NO CONTESTAR"


if h >= 14 and h < 17:
    r = "NO CONTESTAR"


n = str(n)




if h >= 17 and h <= 19 and n.startswith("877"):
    r = "NO CONTESTAR"   
elif h >= 17 and h <= 19:
    r = "CONTESTAR"   


if h > 19:
    r = "NO CONTESTAR"


print("RESULTADO: ",r)     