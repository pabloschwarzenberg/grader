      #Contestador de celular


#declaro variables -- pido valores al usuario
numtel = int( input("ingrese telefono :"))
hora   = int( input("ingrese hora :"))


#SI hora mayor 00  Y hora menor 07                            -- contestar
if (hora > 0) and (hora < 7):
 print("contestar")

#SI hora menor 14 and fin del numero = 909                    -- contestar
elif hora < 14 and (numtel%1000)== 909:
 print("contestar")
            

#SI hora menor 14 and fin del numero != 909                   -- no contestar
elif hora < 14 and (numtel%1000)!= 909:
 print("no contestar")

#SI HORA MAYOR 17 Y hora menor 19 Y  inicio numero = 877      -- contestar
elif hora > 17 and hora < 19 and round(numtel/100000)==877:
 print("contestar")

#SI HORA MAYOR 17 Y hora menor 19 Y hora inicio numero != 877 -- no contestar
elif hora > 17 and hora < 19 and round(numtel/100000)!= 877:
 print("no contestar")

#SI HORA mayor 19                                             -- no contestar
elif hora > 19:
 print("no contestar")