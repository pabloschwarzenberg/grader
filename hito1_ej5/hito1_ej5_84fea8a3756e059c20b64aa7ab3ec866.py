#Cálculo del dígito verificador de un rut

rut = int(input("Ingrese un rut sin digito verificador: "))


dig1 = rut // 10000000
rut = rut - (dig1*10000000)

dig2 = rut // 1000000
rut = rut - (dig2*1000000)

dig3 = rut // 100000
rut = rut - (dig3*100000)

dig4 = rut // 10000
rut = rut - (dig4*10000)

dig5 = rut // 1000
rut = rut - (dig5*1000)

dig6 = rut // 100
rut = rut - (dig6*100)

dig7 = rut // 10
rut = rut - (dig7*10)
    
dig8 = rut
    
dig8 = dig8 * 2
dig7 = dig7 * 3
dig6 = dig6 * 4
dig5 = dig5 * 5
dig4 = dig4 * 6
dig3 = dig3 * 7
dig2 = dig2 * 2
dig1 = dig1 * 3
    
suma = dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7 + dig8
x = suma // 11
y = suma - (11 * x)
z = 11 - y
if z == 11:
        dv = 0
        print("dv=0")
        
if z == 10:
        dv = "K"
        print("dv=K")
        
if 0 <= z <= 9:
        dv = z
        print("dv=",z)