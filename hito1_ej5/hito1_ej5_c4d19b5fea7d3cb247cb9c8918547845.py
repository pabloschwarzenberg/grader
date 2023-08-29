rut = input("Ingrese su rut: ")
ter = str(rut)

a = int(ter[0])
b = int(ter[1])
c = int(ter[2])
d = int(ter[3])
e = int(ter[4])
f = int(ter[5])
g = int(ter[6])

    
  
if(len(ter)== 8):
    h = int(ter[7])
    sf = a*3 + b*2 + c*7 + d*6 + e*5 + f*4 + g*3 + h*2
    r = sf%11
    dv = 11 - r
    
else:
    sf = g*2 + f*3 + e*4 + d*5 + c*6 + b*7 + a*2
    r = sf%11
    dv = 11 - r

if(dv == 10):
    print ("dv = k")
elif(dv == 11):
    print ("dv =",0)
else:
    print("dv =",dv)
