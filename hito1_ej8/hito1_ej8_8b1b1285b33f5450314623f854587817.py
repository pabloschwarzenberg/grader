num=str(input("Ingrese número :"))
if len(num)==1:
    print(str(num)+"U")
if len(num)==2:
    print(str(num[-2]+"D")+"+"+str(num[-1])+"U")
if len(num)==3:
    print(str(num[-3])+"C"+"+"+str(num[-2]+"D")+"+"+str(num[-1])+"U")
if len(num)==4:
    print(str(num[-4])+"M"+"+"+str(num[-3])+"C"+"+"+str(num[-2]+"D")+"+"+str(num[-1])+"U")
