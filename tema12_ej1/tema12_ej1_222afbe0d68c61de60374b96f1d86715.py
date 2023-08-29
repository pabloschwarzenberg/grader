lista=[]
def per(a,b=''):
        
        global lista
        if len(a)<=1:
            c= b + a
            if c not in lista:
                lista.append(c)
        else:
            for i in range(len(a)):
                antes= a[0:i]
                despues= a[i+1:]
                per(antes + despues,b + a[i])
n=int(input('ingrese: '))
palabra=[]
for i in range(0,n):
    palabra.append('0')
lista.append(palabra)
for i in range(0,n):
    palabra[i]='1'
    per(''.join(palabra))
for a in lista:
  print(a)