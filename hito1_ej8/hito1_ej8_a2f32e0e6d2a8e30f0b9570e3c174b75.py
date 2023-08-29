#Descomponer un número
nu= input("Ingrese un numero de hasta 4 digitos:")
len_n= len(nu)
if len_n==1:
    print(nu[0]+"U")
elif len_n==2:
    print(nu[0]+"D"+"+"+nu[1]+"U")
elif len_n==3:
    print(nu[0]+"C"+"+"+nu[1]+"D"+"+"+nu[2]+"U")
elif len_n==4:
    print(nu[0]+"M"+"+"+nu[1]+"C"+"+"+nu[2]+"D"+"+"+nu[3]+"U")