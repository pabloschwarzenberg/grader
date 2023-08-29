#Contestador de celular
n=int(input("ingrese numero telefonico:"))
h=int(input("ingrese hora de llamada:"))

if (0<h<=7):
    print("CONTESTAR")

if(8<h<=14)and(((n-(n//1000)*1000)))==909:
    print("CONTESTAR")
else:
        print("NO CONTESTAR")

if(17<=h<=19)and((n//100000)==878):
    print("NO CONTESTAR")

if (19<h):
    print("NO CONTESTAR")
  
      
        
