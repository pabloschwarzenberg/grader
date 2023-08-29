b = int(input("numero de telefono: "))
a = int(input("hora: "))
string = str(b)
if 0<a<7:
    print("CONTESTAR")
if a < 14 and string[5:] == "909":
    print("CONTESTAR")
if  17<a<19 and string[:3] == "877":
    print("NO CONTESTAR")

if  17<a<19 and string[:3] == "877":
    print("NO CONTESTAR")
if 19<a<23:
    print("NO CONTESTAR")
