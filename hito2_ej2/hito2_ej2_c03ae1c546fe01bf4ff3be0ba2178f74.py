ADN1= input("ADN1: ")
contador = 0
for i in range(0,len(ADN1)):
    if not ADN1[i].upper == "A" or ADN1[i].upper == "T" or ADN1[i].upper == "C" or ADN1[i].upper == "G":
        print("secuencia incorrecta")
        break
    else:
        contador = 0
if contador == 0:
    print("secuencia correcta")