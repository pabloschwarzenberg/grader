#signo zodiacal

print("---------- Ingrese su dia de nacimiento ----------")
dia_nacimiento = int((input("Día: ")))
print("---------- Ingrese su mes de nacimiento ----------")
mes_nacimiento = int(input("Mes: "))

cap = "capricornio"
acu = "acuario"
pis = "piscis"
ari = "aries"
tau = "tauro"
gem = "geminis"
can = "cancer"
leo = "leo"
vir = "virgo"
lib = "libra"
esc = "escorpio"
sag = "sagitario"


if mes_nacimiento == 12 and dia_nacimiento > 22 or mes_nacimiento == 1 and dia_nacimiento <= 20:
    print("---Eres signo---")
    print(cap)
    
if mes_nacimiento == 1 and dia_nacimiento > 20 or mes_nacimiento == 2 and dia_nacimiento <= 19:
    print("---Eres signo---")
    print(acu)
    
if mes_nacimiento == 2 and dia_nacimiento > 19 or mes_nacimiento == 3 and dia_nacimiento <= 21:
    print("---Eres signo---")
    print(pis)
    
if mes_nacimiento == 3 and dia_nacimiento < 21 or mes_nacimiento == 4 and dia_nacimiento <= 20:
    print("---Eres signo---")
    print(ari)
    
if mes_nacimiento == 4 and dia_nacimiento < 20 or mes_nacimiento == 5 and dia_nacimiento <= 21:
    print("---Eres signo---")
    print(tau)
    
if mes_nacimiento == 5 and dia_nacimiento < 21 or mes_nacimiento == 6 and dia_nacimiento <= 21:
    print("---Eres signo---")
    print(gem)
    
if mes_nacimiento == 6 and dia_nacimiento < 21 or mes_nacimiento == 7 and dia_nacimiento <= 21:
    print("---Eres signo---")
    print(can)
    
if mes_nacimiento == 7 and dia_nacimiento < 23 or mes_nacimiento == 8 and dia_nacimiento <= 23:
    print("---Eres signo---")
    print(leo)
    
if mes_nacimiento == 8 and dia_nacimiento < 23 or mes_nacimiento == 9 and dia_nacimiento <= 23:
    print("---Eres signo---")
    print(vir)
    
if mes_nacimiento == 9 and dia_nacimiento < 23 or mes_nacimiento == 10 and dia_nacimiento <= 23:
    print("---Eres signo---")
    print(lib)
    
if mes_nacimiento == 10 and dia_nacimiento < 23 or mes_nacimiento == 11 and dia_nacimiento <= 22:
    print("---Eres signo---")
    print(esc)
    
if mes_nacimiento == 11 and dia_nacimiento < 22 or mes_nacimiento == 12 and dia_nacimiento <= 22:
    print("---Eres signo---")
    print(sag)
    