num = input("Ingrese número de telefono: ")
hora = int(input("Ingrese la hora: "))
pn = int(num[0:3])
fn = int(num[5:8])
if hora >= 0 and hora <= 7 or hora > 7 and hora < 14 and fn == 909:
    print("Contestar")
    if hora > 7 and hora < 14 and fn != 909:
        print("No contestar")

if hora >= 14 and hora < 17 or hora > 19 and hora < 23 :
    print("No contestar")
    
if hora >= 17 and hora <= 19 and pn == 877:
    print("No contestar")
    if hora >= 17 and hora <= 19 and pn != 877:
        print("Contestar")
