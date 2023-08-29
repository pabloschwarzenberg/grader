#Conversión de Decimal a Binario
#esto es mas facil 
#numero = int(input("Ingrese el numero: "))
#resultado = format(numero, "0b")
#print("resultado=" + str(resultado))
#pero aca dejo el programa sin siclo
numero = int(input("Ingrese un numero: "))
x = numero%2
if numero == 0:
    print("resultado="+str(0))
elif numero == 1:
    print("resultado="+str(1))
elif numero == 2:
    print("resultado="+str(10))
elif numero == 3:
    print("resultado="+str(11))
elif (x==1 or x==0) and numero <= 7 and numero >=4:
    q = numero//2 
    w = q*2 
    e = numero-w 
    r = q//2 
    t = r*2 
    y = q-t 
    u = r//2 
    i = u*2 
    o = r - i 
    print("resultado="+str(o)+str(y)+str(e))
elif (x == 1 or x == 0 ) and numero <= 31 and numero > 15:
    q = numero//2 #23//2
    w = q*2 # q = 11 --- 11*2 = 22
    e = numero-w # 23 - 22 = [1]
    r = q//2 # 11//2 = 5
    t = r*2 #  5 * 2 = 10
    y = q-t # 11-10 = [1]
    u = r//2 # 5//2 = 2
    i = u*2 # 2*2 = 4
    o = r - i # 5 -4 = [1]
    p = u//2 # 2//2 = 1
    a = p * 2 # 1 * 2= 2
    s = u - a # 2 - 2 = [0]
    d = p//2 # 1//2 = 0
    f = p - d # 1 - 0 = [1] 
    print("resultado="+str(f)+str(s)+str(o)+str(y)+str(e))
elif (x == 1 or x == 0) and numero > 29 and numero < 64:
    q = numero//2 # 33//2 = 16
    w = q*2 # 16 * 2 = 32
    e = numero-w # 33 - 32 = [1] 
    r = q//2 # 16//2 = 8 
    t = r*2 #  8*2 = 16
    y = q-t # 16 -16 = [0]
    u = r//2 # 8//2 = 4
    i = u*2 # 4*2 = 8
    o = r - i # 8 -  8 = [0]
    p = u//2 # 4//2 = 2
    a = p * 2 # 2 * 2 = 4
    s = u - a  # 4 - 4 = [0]
    d = p//2 # 2//2 = 1
    f = d * 2 # 1 * 2 = 2
    g = p - f # 2 - 2 = [0]
    h = d//2 # 1//2 = 0
    j = h * 2 # 0 * 2 = 0
    k = d - j # 1 - 0 = [1]
    print("resultado="+str(k)+str(g)+str(s)+str(o)+str(y)+str(e))
elif (x == 1 or x == 0 ) and numero <= 15 and numero >7:
    q = numero//2 
    w = q*2 
    e = numero-w 
    r = q//2 
    t = r*2 
    y = q-t 
    u = r//2 
    i = u*2 
    o = r - i 
    p = u//2 
    a = p * 2 
    s = u - a 
     
    print("resultado="+str(s)+str(o)+str(y)+str(e))
else:
  if (x == 1 or x == 0) and numero >= 64 and numero <= 100:
    
    q = numero//2 # 64//2=32
    w = q*2 # 32*2=64
    e = numero-w # 64-64=[0]
    r = q//2 #32//2=16  
    t = r*2 #  16*2=32
    y = q-t # 32-32=[0]
    u = r//2 # 16//2=8
    i = u*2 # 8*2=16
    o = r - i # 16-16=[0]
    p = u//2 # 8//2=4
    a = p * 2 # 4*2=8
    s = u - a  # 8-8=[0]
    d = p//2 # 4//2=2
    f = d * 2 # 2*2=4
    g = p - f # 4-4=[0]
    h = d//2 # 2//2=1
    j = h * 2 #1*2=2
    k = d - j # 2-2=[0]
    l = h//2#1//2=0
    ñ = l*2#0*2=0
    z = h-ñ#1-0=[1]
    print("resultado="+str(z)+str(k)+str(g)+str(s)+str(o)+str(y)+str(e))
