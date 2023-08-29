numero=(input("Ingrese el numero: "))
numero=float(numero)

#Descomponer
m= numero//1000
m=float(m)
c= numero//100
c=float(c)
cf= c%10
cf=float(cf)
d=numero//10
d=float(d)
df= d%10
df=float(df)
u= numero%100
u=float(u)
uf =u%10
uf=float(uf)
#Final
if numero>=1000:
    print(int(m),str("M"),"+",int(cf),str("C"),"+",int(df),str("D"),"+",int(uf),str("U"))
    
if numero<=999:
    print(int(cf),str("C"),"+",int(df),str("D"),"+",int(uf),str("U"))
    
if numero<=99:
    print(int(df),str("D"),"+",int(uf),str("U"))

if numero<=9:
    print(int(uf),str("U"))
