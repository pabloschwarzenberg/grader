#Zodiaco
dia=int(input())
m=int(input())
if m == 1:
  dia = dia
if m == 2: 
  dia = dia + 31
if m == 3:
  dia = dia + 59
if m == 4:
  dia = dia + 90
if m == 5:
  dia = dia + 120
if m == 6:
  dia = dia + 151
if m == 7:
  dia = dia + 181
if m == 8:
  dia = dia + 212
if m == 9:
  dia = dia + 243
if m == 10:
  dia = dia + 273
if m == 11:
  dia = dia + 304
if m == 12:
  dia = dia + 334
for dia in range(1, 365):
  if dia >= 80 and dia <= 110:
    print("Aries")
  if dia >= 111 and dia <= 141:
    print("Taurus")
  if dia >= 142 and dia <= 172:
    print("Gemini")
  if dia >= 173 and dia <= 203:
    print("Cancer")
  if dia >= 204 and dia <= 234:
    print("Leo")
  if dia >= 235 and dia <= 266:
    print("Virgo")
  if dia >= 267 and dia <= 296:
    print("Libra")
  if dia >= 297 and dia <= 326:
    print("Scorpio")
  if dia >= 327 and dia <= 355:
    print("Sagittarius")
  if dia >= 356 and dia <= 365 and dia >= 1 and dia <= 20:
    print("Capricorn")
  if dia >= 21 and dia <= 50:
    print("Aquarius")
  if dia >= 51 and dia <= 79:
    print("Pisces")