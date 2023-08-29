
n=(int(input("Ingrese su numero de telefono: ")))
h=(int(input("Ingrese la hora: ")))
c=str(n)
d=str(h)
x=0

while(x<1):
    if(len(c)==8):
      x=x=1
      print()
    elif(len(c)>8):
        print("valor valido")



for i in range(0,23):
    if(h<=0 and h<7):
        print("Contestar ya que podría ser una emergencia")
    elif(h<14 and c[5]=="9" and c[6]=="0" and c[7]=="9"):
        print("Contestar")
    elif(h>=17 and h<=19):
        print("No Contestar")
        if(c[0]=="8" and c[1]=="7" and c[2]=="7"):
            print("No Contestar")
        else:()
        print("Contestar")
    elif(h>19):
        print("No Contestar")
