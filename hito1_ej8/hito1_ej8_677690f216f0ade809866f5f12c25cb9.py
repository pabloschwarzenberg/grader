#Descomponer un número
numero=int(input("Ingrese un numero de hasta 4 cifras:"))

respaldo=numero

d1=numero%10
numero=numero//10

d2=numero%10
numero=numero//10

d3=numero%10
numero=numero//10

d4=numero%10
numero=numero//10

if 1<= respaldo <=9:
    cadenadecaracteres=str(d1)+"U"
    print(cadenadecaracteres)
    
elif 10<= respaldo <=99:
    cadenadecaracteres=str(d2)+"D+"+str(d1)+(U)
    print(cadenadecaracteres)
    
elif 100<= respaldo <=999:
    cadenadecaracteres=str(d3)+"C+"+str(d2)+"D+"+str(d1)+"U"
    print(cadenadecaracteres)
    
elif 1000<= respaldo <=9999:
     cadenadecaracteres=str(d4)+"M+"+str(d3)+"C+"+str(d2)+"D+"+str(d1)+"U"
     print(cadenadecaracteres)
     
print(" d4, d3, d2, d1 ")