#Cálculo del dígito verificador de un rut
m = [2,3,4,5,6,7]
dvs = ["0","1","2","3","4","5","6","7","8","9","k"]
rutt = []
rut = input("Ingrese rut sin digito verificador ni puntos: ")
i = 0
vt = 0
mul = 0
pos = 0
while True:
    num = rut[i:i+1]
    if num == '':
        pos = len(rutt)-1
        while True:
            if mul <= 5:
                vt = vt + (rutt[pos]*m[mul])
                mul += 1
                pos -= 1
            else:
                mul = 0
            if pos < 0:
                break 
        vtt = vt/11
        vtt = int(vtt)
        vtt = vt - (vtt * 11)
        vtt = 11 - vtt
        if vtt == 11:
            dvv = "0"
            break
        elif vtt == 10:
            dvv = "k"
            break
        else:
            dvv = vtt
            break
    else:
        rutt.append(int(num))
        i += 1
print(dvv)