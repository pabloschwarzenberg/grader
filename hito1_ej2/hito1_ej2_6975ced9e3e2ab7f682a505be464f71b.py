n=input("ingrese el numero: ")  #numero
h=int(input("ingrese la hora: "))    #hora
lista=[]
for i in n:
    lista.append(int(i))

if 0<h<7:
    print("CONTESTAR")
elif h<14 and (n[5]=="9") and (n[6]=="0") and (n[7]=="9"):
    print("CONTESTAR")
elif 17<h<19 and not (n[0]=="8") and not (n[1]=="7") and not (n[2]=="7"):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
if h>19:
    print("NO CONTESTAR")

