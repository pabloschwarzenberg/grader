#Descomponer un número
numero = int(input("Ingrese un numero de 4 dígitos")) #1230
n_codigo = str(numero) #"1230"
codigo = ((n_codigo)[::-1]) # "0321"
tamaño = len(n_codigo) #4

digito1 = "UDCM"
digito2 = "UDC"
digito3 = "UD"
digito4 = "U"

limite1 = 1
limite2 = 2
limite3 = 3
limite4 = 4

U = ""
D = ""
C = ""
M = ""

verificador = ""
if(not(U == "0") and tamaño >= limite1):
    valor = codigo[0]
    U = valor
    U = U + "U"
    verificador = verificador + "U"
else:
    U = ""

if(not(D == "0") and tamaño >= limite2):
    valor = codigo[1]
    D = valor
    D = D + "D"
    verificador = verificador + "D"
else:
    D = "" 

if(not(C == "0") and tamaño >= limite3):
    valor = codigo[2]
    C = valor
    C = C + "C"
    verificador = verificador + "C"
else:
    C = ""
if(not(M == "0") and tamaño >= limite4):
    valor = codigo[3]
    M = valor
    M = M + "M"
    verificador = verificador + "M"

else:
    M = ""

if(verificador == digito1):
    print(M,"+",C,"+",D,"+",U)

if(verificador == digito2):
    print(C,"+",D,"+",U)

if(verificador == digito3):
    print(D,"+",U)

if(verificador == digito4):
    print(U)
      