#Contestador de celular
num_tel = 0 
hora = -1
resul = "Sin llamada"
ult_dig = 0
prim_dig = 0

while len(str(num_tel)) != 8:
    print("Ingrese numero telefonico Válido (8 caracteres):")
    num_tel = int(input())
    ult_dig = str(num_tel)[5:8]
    prim_dig = str(num_tel)[0:3]
    continue
while hora < 0 or hora > 23:
    print("Ingrese hora de la llamada entre 0 y 23 hrs:")
    hora = int(input())
    continue
if hora >= 0 and hora <= 6:
    resul = "CONTESTAR"
    print(resul)
elif hora >= 17 and hora <= 19 and int(prim_dig) != 877:
    resul = "CONTESTAR"
    print(resul)
elif hora <= 14 and int(ult_dig) == 909:
     resul = "CONTESTAR"
     print(resul)
else:
    resul = "NO CONTESTAR"
    print(resul)     