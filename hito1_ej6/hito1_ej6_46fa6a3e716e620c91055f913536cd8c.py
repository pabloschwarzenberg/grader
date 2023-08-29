#Ordenar tres números
G = int(input("ingrese le primer numere"))
O = int(input("igrese le segunde numere"))
S = int(input("ingrese le tercer numere"))
Ma = max(G,O,S)
Mi= min(G,O,S)
D = (G+O+S) - Ma - Mi
print(- Ma - Mi)
print (Mi,",",D,",",Ma)