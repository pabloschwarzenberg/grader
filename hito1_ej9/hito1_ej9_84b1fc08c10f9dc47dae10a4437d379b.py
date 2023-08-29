num = input("Ingrese 6 numeros para la ecuacion: ")
num = list(num)

if len(num) != 6:
    print("ERROR")
else:
    x = (num[4]*num[2]-num[1]*num[5])/(num[4]*num[0]-num[1]*num[3])
    y = (num[5]-num[3]*x)/num[4]
    
    res = []
    x = "x="+str(round(x, 1))
    y = "y="+str(round(y, 1))
    res.append(x)
    res.append(y)
    print(res)