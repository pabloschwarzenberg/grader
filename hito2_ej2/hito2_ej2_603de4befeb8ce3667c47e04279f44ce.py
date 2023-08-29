lista = ["a","c","t","g"]
sec = str(input("Secuencia: "))
sec1 = sec.lower()
print(sec1)
ver = ""
cont = 0
for elem in sec1:
    if elem in lista:
        cont = cont + 1
if cont == len(sec):
    ver = "correcta"
else:
    ver = "incorrecta"
if ver == "correcta":
    print("La secuencia {} es correcta".format(sec))    
elif ver == "incorrecta":
    print("La secuencia {} es incorrecta".format(sec))