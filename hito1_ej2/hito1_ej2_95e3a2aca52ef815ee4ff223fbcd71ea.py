#Contestador de celular
fono=int(input(""))
n1=(fono//10000000)
n2= ((fono-(n1*10000000))//1000000)
n3=((fono-(n1*10000000+n2*1000000))//100000)
n4=((fono-(n1*10000000+n2*1000000+n3*100000))//10000)
n5=((fono-(n1*10000000+n2*1000000+n3*100000+n4*10000))//1000)
n6=((fono-(n1*10000000+n2*1000000+n3*100000+n4*10000+n5*1000))//100)
n7=((fono-(n1*10000000+n2*1000000+n3*100000+n4*10000+n5*1000+n6*100))//10)
n8=(fono-(n1*10000000+n2*1000000+n3*100000+n4*10000+n5*1000+n6*100+n7*10))

hora=int(input(""))

sumafin=(n6*100+n7*10+n8)
sumainicial=(n1*100+n2*10+n3)

if (0<=hora<=7)==True:
    print("CONTESTAR")

elif (7<hora<14 and sumafin==909)==True:
    print("CONTESTAR")

elif (17<=hora<=19 and sumainicial!=877)==True:
    print("CONTESTAR")

elif (hora>19)==True:
    print("NO CONTESTAR")

else:
    print("NO CONTESTAR")
