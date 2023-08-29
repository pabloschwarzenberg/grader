#Contestador de celular

numero = int(input(">>>Ingrese número telefónico: "))

hora = int(input(">>>Ingrese hora de la llamada: "))

dig1 = numero // 10000000
numero = numero - (dig1*10000000)

dig2 = numero // 1000000
numero = numero - (dig2*1000000)

dig3 = numero // 100000
numero = numero - (dig3*100000)

dig4 = numero // 10000
numero = numero - (dig4*10000)

dig5 = numero // 1000
numero = numero - (dig5*1000)

dig6 = numero // 100
numero = numero - (dig6*100)

dig7 = numero // 10
numero = numero - (dig7*10)

dig8 = numero

if 0 <= hora <= 7:
    print(">>>CONTESTAR")
    
elif (dig6 == 9 and dig7 == 0 and dig8 == 9) and (8 <= hora <= 14):
    print(">>>CONTESTAR")
    
elif 8 <= hora <= 14:
    print(">>>NO CONTESTAR")
    
elif 15 <= hora <= 16:
    print(">>>NO CONTESTAR")
    
elif (dig1 == 8 and dig2 == 7 and dig3 == 7) and (17 <= hora <= 19):
    print(">>>NO CONTESTAR")
    
elif 17 <= hora <= 19:
    print(">>>CONTESTAR")
    
elif 18 <= hora <= 23:
    print(">>>NO CONTESTAR")
    
else:
    print("ERROR")
    input()