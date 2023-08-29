#Entradas
rut = (input("Ingrese el rut: "))
digitos = len(rut)
rut = int(rut)


if digitos == 7:
    d1 = rut // 10**6
    d2_temp = rut // 10**5
    d2 = d2_temp % d1*10
    d3_temp = rut // 10**4
    d3 = d3_temp % d2_temp
    d4_temp = rut // 10**3
    d4 = d4_temp % d3_temp
    d5_temp = rut // 10**2
    d5 = d5_temp % d4_temp
    d6_temp = rut // 10
    d6 = d6_temp % d5_temp
    d7 = rut % d6_temp
    
    suma = (d7 * 2) + (d6 * 3) + (d5 * 4) + (d4 * 5) + (d3 * 6) + (d2 * 7) + (d1 * 2) 

    dv = 11 - (suma % 11)  

    if dv==11:
        print("dv=",0)
    elif dv==10:
        print("dv=","K")
    else:
        print ("dv=",dv)    
    
  
    
#Procedimiento
d1 = rut // 10000000
d2_temp = rut // 1000000
d2 = d2_temp - d1 * 10
d3_temp = rut // 100000
d3 = d3_temp % d2_temp
d4_temp = rut // 10000
d4 = d4_temp % d3_temp
d5_temp = rut // 1000
d5 = d5_temp % d4_temp
d6_temp = rut // 100
d6 = d6_temp % d5_temp
d7_temp = rut // 10
d7 = d7_temp % d6_temp
d8 = rut % d7_temp

print(d1,d2,d3,d4,d5,d6,d7,d8)

suma =(d8 * 2) + (d7 * 3) + (d6 * 4) + (d5 * 5) + (d4 * 6) + (d3 * 7) + (d2 * 2) + (d1 * 3)

dv = 11 - (suma % 11)  

if dv==11:
    print("dv=",0)
elif dv==10:
    print("dv=","K")
else:
    print ("dv=",dv-1)    