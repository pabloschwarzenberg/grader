def jerigonzo(palabra):
 palabra=palabra.lower()
 largo=len(palabra)
 i=0
 respuesta=str()
 while i<largo:
     letra=palabra[i]
     respuesta=respuesta+letra
     if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
         respuesta=respuesta+"p"+letra
     i=i+1

 return respuesta


         