
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import random
import codecs

chance = 10
file = codecs.open('dic.txt',encoding='utf-8')
lines = file.readlines()
file.close()
msg = lines[random.randint(0,len(lines))]
aux=["_"]*(len(msg)-1)
print ''.join(aux)
while chance > 0:
        letra = raw_input(">>")
        acerto = False
        for j, l in enumerate(msg):
                if l == letra:
                        aux[j]=l
                        acerto = 1
        if acerto:
                print "Bien!"
        else:
                print "Muy mal!"
                chance -= 1
        print ''.join(aux)
        if '_' not in aux:
                print "Lo lograste!"
                break
print "Los sentimos se le acabaron los turnos!"
print "La palabra era " + msg 
def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
         