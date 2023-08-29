p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
l=[]
contador_veinte=0
contador_quince=0
aplica_descuento1=0
aplica_descuento2=0
aplica_descuento3=0
aplica_descuento4=0
aplica_descuento5=0
while True:
    a=input()
    if a=="ver":
        print(l)
    elif a=="checkout":
        break
    b=a.split(",")
    if b[0]=="1":
        l.append(p1*(int(b[1])))
        contador_veinte+=(p1[2]*(int(b[1])))
        aplica_descuento1+=1
    elif b[0]=="2":
        l.append(p2*(int(b[1])))
        contador_veinte+=(p2[2]*(int(b[1])))
        aplica_descuento2=1
    elif b[0]=="3":
        l.append(p3*(int(b[1])))
        contador_veinte+=(p3[2]*(int(b[1])))
        aplica_descuento3+=1
    elif b[0]=="4":
        l.append(p4*(int(b[1])))
        contador_quince+=(p4[2]*(int(b[1])))
        aplica_descuento4+=1
    elif b[0]=="5":
        l.append(p5*(int(b[1])))
        contador_quince+=(p5[2]*(int(b[1])))
        aplica_descuento5+=1

if aplica_descuento1==aplica_descuento2==aplica_descuento3:
    contador_veinte=(contador_veinte)-(contador_veinte*0.2)
if aplica_descuento4==aplica_descuento5:
    contador_quince=(contador_quince)-(contador_quince*0.15)
print(round((contador_veinte+contador_quince),1))