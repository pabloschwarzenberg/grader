a=input()
def suma_precios(a):
 z=[]
 s=0
 if a=="ver":
     print("""
[1,"Pokemon X",33.77]
[2,"Nintendo XL",203]
[3,"Mario Kart 7",27.58]
[4,"PlayStation 4",348.00]
[5,"FIFA 16",51.19]""")
     a=input()
 
 while a!='checkout':
  if a[0]=='1':
    z.append(a)
    b=float(33.77) * int(a[2])
    s=b+s
    a=input()
  elif a[0]=='2':
    z.append(a)
    b= float(203.00) * int(a[2])
    s=b+s
    a=input()
  elif a[0]=='3':
    z.append(a)
    b= float(27.58) * int(a[2])
    s=b+s
    a=input()
  elif a[0]=='4':
    z.append(a)
    b= float(348.00) * int(a[2])
    s=b+s
    a=input()
  elif a[0]=='5':
    z.append(a)
    b= float(51.19) * int(a[2])
    s=b+s
    a=input()
 z.append(s)
 return(z)

def descuento(z):
  if(z[-2][0]=='1' or z[-3][0]=='1' or z[-4][0]=='1')and(z[-2][0]=='2' or z[-3][0]=='2' or z[-4][0]=='2')and(z[-2][0]=='3' or z[-3][0]=='3' or z[-4][0]=='3'):
     y=int(z[-1]) - ((20*(int(z[-1])))/100)
     z.remove(z[-1])
     z.append(y)
     return round(z[-1],1)
  elif(z[-2][0]=='4' or z[-3][0]=='4' or z[-4][0]=='4')and(z[-2][0]=='5' or z[-3][0]=='5' or z[-4][0]=='5'):
     y=int(z[-1]) - ((15*(int(z[-1])))/100)
     z.remove(z[-1])
     z.append(y)
     return round(z[-1],1)
  else:
     return round(z[-1],1)

print(descuento(suma_precios(a)))

 