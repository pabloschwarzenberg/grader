#Contestador de celular
n = str(input("Ingrese el número telefónico: "))
h = int(input("Ingrese la hora del día: "))

if h > 0: 
    if h < 7:
        print ("CONTESTAR")
if h < 14:
    if h > 7:
        if str(n[-3]) == '9':
            if str(n[-2]) == '0':
                if str(n[-1]) == '9':
                    print ("CONTESTAR")
    else: 
        print ("NO CONTESTAR")
if h > 17:
    if h < 19:
        if str(n[0:1]) == '8':
            if str(n[1:2]) == '7':
                if str(n[2:3]) == '7':
                    print ("NO CONTESTAR")
    else:
        print ("CONTESTAR")
if h > 19:
    if h < 23:
        print ("NO CONTESTAR")