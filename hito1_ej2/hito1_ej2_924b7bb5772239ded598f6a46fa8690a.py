#Contestador de celular

cellphone_number = input("Telefono: ")
hour = int(input("Hora: "))

answer_call = False

if hour >= 0 and hour <= 7:
    answer_call = True
elif hour < 14 and cellphone_number[-3:] == "909":
    answer_call = True
elif hour >= 17 and hour <= 19 and not cellphone_number.startswith("877"):
    answer_call = True

# Print the result
if answer_call:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")