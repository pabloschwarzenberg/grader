#Contestador de celular
numero=input("ingrese su numero:")

largo=len(numero)

lista=list(numero)



if largo<8:
    print("su numero debe ser de 8 digitos")
elif largo>8:
    print("Su numero debe ser de 8 digitos")


hora=int(input("Ingrese su hora:"))

if hora==0:
    print("CONTESTAR")
elif hora==1:
    print("CONTESTAR")
elif hora==3:
    print("CONTESTAR")
elif hora==4:
    print("COntestar")
elif hora==5:
    print("CONTESTAR")
elif hora==6:
    print("CONTESTAR")
elif hora==7:
    print("CONTESTAR")
elif hora==8 and lista[5]==9 and lista[6]==0 and lista[7]==9:
    print("CONTESTAR")
elif hora==9 and lista[5]==9 and lista[6]==0 and lista[7]==9:
    print("CONTESTAR")
elif hora==10 and lista[5]==9 and lista[6]==0 and lista[7]==9 :
    print("CONTESTAR")
elif hora==11 and lista[5]==9 and lista[6]==0 and lista[7]==9:
    print("CONTESTAR")
elif hora==12 and lista[5]==9 and lista[6]==0 and lista[7]==9:
    print("CONTESTAR")
elif hora==13 and lista[5]==9 and lista[6]==0 and lista[7]==9:
    print("CONTESTAR")
elif hora==8 and lista[5]!=9 and lista[6]!=0 and lista[7]!=9:
    print("CONTESTAR")
elif hora==9 and lista[5]!=9 and lista[6]!=0 and lista[7]!=9:
    print("CONTESTAR")
elif hora==10 and lista[5]!=9 and lista[6]!=0 and lista[7]==9 :
    print("CONTESTAR")
elif hora==11 and lista[5]!=9 and lista[6]!=0 and lista[7]!=9:
    print("CONTESTAR")
elif hora==12 and lista[5]!=9 and lista[6]!=0 and lista[7]!=9:
    print("CONTESTAR")
elif hora==13 and lista[5]!=9 and lista[6]!=0 and lista[7]!=9:
    print("CONTESTAR")
elif hora==14:
    print("CONTESTAR")
elif hora==15:
    print("CONTESTAR")
elif hora==16:
    print("CONTESTAR")
elif hora==17 and lista[5]!=8 and lista[6]!=7 and lista[7]!=7:
    print("NO CONTESTAR")
elif hora==18 and lista[5]!=8 and lista[6]!=7 and lista[7]!=7:
    print("NO CONTESTAR")
elif hora==19 and lista[5]!=8 and lista[6]!=7 and lista[7]!=7:
    print("NO CONTESTAR")
elif hora==17 and lista[5]==8 and lista[6]==7 and lista[7]==7:
    print("CONTESTAR")
elif hora==18 and lista[5]==8 and lista[6]==7 and lista[7]==7:
    print("CONTESTAR")
elif hora==19 and lista[5]==8 and lista[6]==7 and lista[7]==7:
    print("CONTESTAR")
elif hora==20:
    print("NO CONTESTAR")
elif hora==21:
    print("NO CONTESTAR")
elif hora==22:
    print("NO CONTESTAR")
elif hora==23:
    print("NO CONTESTAR")
elif hora==24:
    print("NO CONTESTAR")