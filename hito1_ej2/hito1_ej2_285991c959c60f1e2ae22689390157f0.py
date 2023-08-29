#Contestador de celular
N=int(input("Ingrese numero:"))
H=int(input("Ingrese hora:"))

n1=(N%1000)
n2=(N//100000)

if(0<H<=7)or((8<H<=14)and(n1==909))or((17<H<=19)and(n2!=877)):
    print("CONTESTAR")
      
else:
    print("NO CONTESTAR")

