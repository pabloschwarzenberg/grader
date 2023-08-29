numeroDecimal = int(input('Introduce el número a convertir a binario: '))
binario = ""
while numeroDecimal > 0:  #33>0;
    #print(numeroDecimal % 2)
    numero = numeroDecimal % 2  #=33%2= 1; =16%2= 0; =8%2= 0; =4%2= 0; =2%2= 0; =1%2= 1;
    numeroDecimal = numeroDecimal // 2 #=33//2=16; =16//2=8; =8//2=4; =4//2=2; =2//2=1; =1//2=0;
    binario = str(numero) + binario  #acumulador binario: 1; 10; 100; 1000; 10000; 100001
print("resultado =",binario)
      