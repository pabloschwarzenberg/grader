number= input("Ingrese un numero de hasta 4 digitos:")
len_n= len(number)
if len_n==1:
    print(":",number[0]+ "U")
elif len_n==2:
    print(":",number[0]+"D"+"+"+number[1]+"U")
elif len_n==3:
    print(":",number[0]+"C"+"+"+number[1]+"D"+"+"+number[2]+"U")
elif len_n==4:
    print(":",number[0]+"M"+"+"+number[1]+"C"+"+"+number[2]+"D"+"+"+number[3]+"U")
