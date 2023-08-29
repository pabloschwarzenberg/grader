#Descomponer un número
num = input()
if len(num) == 4:
  miles = num[-4]+"M"
  cent = num[-3]+"C"
  dec=num[-2]+"D"
  unit=num[-1]+"U"
if len(num) == 3:
  miles = "0M"
  cent = num[-3]+"C"
  dec=num[-2]+"D"
  unit=num[-1]+"U"
if len(num) == 2:
  miles = "0M"
  cent = "0C"
  dec=num[-2]+"D"
  unit=num[-1]+"U"
if len(num)==1:
  miles = "0M"
  cent = "0C"
  dec="0D"
  unit=num[-1]+"U"
print(miles, "+", cent, "+", dec, "+", unit)   