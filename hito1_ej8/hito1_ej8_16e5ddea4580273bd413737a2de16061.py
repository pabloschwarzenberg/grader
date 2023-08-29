num = int(input("Ingrese un numero no mayor de 4 digitos : "))

while num>9999:
    num = int(input("Ingrese un numero no mayor de 4 digitos : "))


mil = num//1000
centena = (num - mil*1000)//100
decena = (num - (mil*1000 + centena*100))//10
unidad = (num - (mil*1000 + centena*100 + decena*10))
if mil>0:
    print(mil,"M + " ,centena ,"C +" ,decena , "D + " ,unidad,"U" )
if mil==0 and centena>0:
    print(centena ,"C +" ,decena , "D + " ,unidad,"U" )
if mil==0 and centena==0 and decena>0:
    print(decena , "D + " ,unidad,"U" )
if mil==0 and centena==0 and decena==0 and unidad>0:
    print(mil,"M + " ,centena ,"C +" ,decena , "D + " ,unidad,"U" )