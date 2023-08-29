#Contestador de celular
 "constans" = {"START_HOUR : "0"
"END_HOUR" : "24"
"RESPONSE_PHONE" : "909"
"NO_RESPONSE_PHONE" : "877"
"PHONE_LENGTH" : "8"
"RESPONSE_STR" : "Resultado: CONTESTAR"
"NO_RESPONSE_STR" : "Resultado: NO CONTESTAR"
"NO_VALID_PHONE" :"Debe ingresar un numero valido (8 dig.)"
"NO_VALID_HOUR": "Debe ingresar una hora valida."}


import constants as cons
def valid_phone():
    while True:
        try:
          phone = int(input(">>>>>> Ingrese número telefónico:\n"))
          if(len(str(abs(phone))) == cons.PHONE_LENGTH ):
            return str(abs(phone))
          else:
            print (cons.NO_VALID_PHONE)
        except ValueError:
          print (cons.NO_VALID_PHONE)

def valid_hora():
    while True:
        try:
          hour = int(input(">>>>>> Ingrese hora de la llamada:\n"))
          if(hour > cons.START_HOUR and hour < cons.END_HOUR ):
            return hour
          else:
            print (cons.NO_VALID_HOUR)
        except ValueError:
          print (cons.NO_VALID_HOUR)  

def Call():
  phone = valid_phone()
  hour = valid_hora()
  if(hour > 0 and hour <= 7 ):
    print (cons.RESPONSE_STR)
  elif (hour > 7 and hour <= 14 ):
    if (phone.endswith(cons.RESPONSE_PHONE)):
      print (cons.RESPONSE_STR)
    else:
      print (cons.NO_RESPONSE_STR)
  elif (hour > 14 and hour <= 17 ):
    print (cons.NO_RESPONSE_STR)
  elif (hour > 17 and hour <= 19 ):
    if (phone.endswith(cons.NO_RESPONSE_PHONE)):
      print (cons.NO_RESPONSE_STR)
    else:
      print (cons.RESPONSE_STR)
  else:
    print (cons.RESPONSE_STR)

Call()
