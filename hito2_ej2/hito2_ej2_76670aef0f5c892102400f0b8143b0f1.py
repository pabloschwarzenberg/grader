string = input()
vdd = False
for i in string:
    if i != "A" and i != "C" and i != "T" and i != "G" :
        vdd = False
        break
    else:
        vdd = True
        
if vdd == True:
    print("La secuencia", string, "es correcta")    
elif vdd == False:
    print("La secuencia", string, "es incorrecta")