print("ingresa la frase que quieres traducir")
mensaje=input()
llave=10  
mode='encryptado'
letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
traducido=''
mensaje=mensaje.upper()
for symbol in mensaje:
    if symbol in letras:
        num=letras.find(symbol)
        if mode=='encryptado':
            num=num+llave
        elif mode=='decriptado':
            num=num-llave
        if num>=len(letras):
            num=num-len(letras)
        elif num<0:
            num=num+len(letras)
        traducido=traducido+letras[num]
    else:
        traducido=traducido+symbol
print(traducido)
