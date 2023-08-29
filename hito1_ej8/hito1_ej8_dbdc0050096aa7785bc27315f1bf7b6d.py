#Descomponer un número
numero = int(input('Escriba el numero que desea descomponer: '))

if numero >= 1000:
     M = numero//1000
     C = (numero-M*1000)//100
     D = ((numero-M*1000)-C*100)//10
     U = (((numero-M*1000)-C*100)-D*10)//1
     M,C,D,U = str(M),str(C),str(D),str(U)
     print(M+'M','+',C+'C','+',D+'D','+',U+'U')     

elif numero >= 100:
     C = numero//100
     D = (numero-C*100)//10
     U = ((numero-C*100)-D*10)//1
     C,D,U = str(C),str(D),str(U)
     print(C+'C','+',D+'D','+',U+'U')      

elif numero >= 10:
     D = numero//10
     U = (numero-D*10)//1
     D,U = str(D),str(U)
     print(D+'D','+',U+'U')   

elif numero >= 1:
     print(str(numero)+'U')             