products = [[1,"Pokemon X",33.77],
            [2,"Nintendo XL",203],
            [3,"Mario Kart 7",27.58],
            [4,"PlayStation 4",348.00],
            [5,"FIFA 16",51.19]]
ui = ""
ui_list = []
carro = 0
while ui != "checkout":
    ui = input(">>> ")
    ui_list.append(ui)
    for item in products:
        if str(item[0]) == ui[0]:
            carro += item[2]*int(ui[2])


for item in ui_list:
    if item[0] == "1":
        for item in ui_list:
            if item[0] == "2":
                for item in ui_list:
                    if item[0] == "3":
                        carro = carro - ((20*carro) / 100)

for item in ui_list:
    if item[0] == "4":
        for item in ui_list:
            if item[0] == "5":
                carro = carro - ((15*carro) / 100)


c = carro % 0.1
d = carro % 1
int_part = carro // 1

if c >= 0.049:
    d += 0.1

carro_redondeado = int_part + d // 0.1 * 0.1

print(ui_list)
print(carro_redondeado)