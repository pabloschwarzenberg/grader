secadn = input("Ingrese una secuenciade ADN: ")
n = int(input("Ingrese el largo: "))
subadn = []
subadnfinal = []
posicionesrepetidas = []

for i in range(len(secadn)):
    if (i+n) > len(secadn):
        break
    
    subadn.append(secadn[i:i+n])

for i in range (len(subadn)): #0 1 2 3 
    for j in range (len(subadn)): # 0 1 2 3 , j = vector
        if (i == (len(subadn)-1)-j):
            break
        
        if (subadn[i] == subadn[(len(subadn)-1)-j]):
            posicionesrepetidas.append(i)
            posicionesrepetidas.append((len(subadn)-1)-i)

for i in range (len(subadn)):
    salto = False
    for j in (posicionesrepetidas):
        if (i == j):
            salto = True
            break
    if (salto):
        continue
    
    else:
        subadnfinal.append(subadn[i])

if (len(subadnfinal) == 0):
    print("ninguna")
    
if (len(subadnfinal) != 0):
    for i in (subadnfinal):
        print(i)

    