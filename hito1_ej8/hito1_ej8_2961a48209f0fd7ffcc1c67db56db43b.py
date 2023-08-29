#Descomponer un número
numero= int(input("Ingrese numero de hasta 4 dijitos:"))
if (numero>0 and numero<99):
    u= numero%10
    d= numero//10
    print(d,"D+",u,"U")
if (numero>99 and numero<999):
    u= numero%10
    d= numero//10 - (numero//100*10)
    c= numero//100
    print(c,"C+",d,"D+",u,"U")
if (numero>999and numero<9999):
    u= numero%10
    d= (numero%100-numero%10)//10
    c= numero//100-(numero//1000*10)
    x= numero//1000
    print(x,"M+",c,"C+",d,"D+",u,"U")