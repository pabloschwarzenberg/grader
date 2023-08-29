#Contestador de celular
fono_numero= int(input("Ingrese numero:"))
llama_hora=  int(input("Digite hora :"))
varl_fono= fono_numero % 1000
varl_fono2= str(fono_numero)
varl_fono2= varl_fono2[0:3]

print(varl_fono2)


if llama_hora >= 0 and llama_hora <= 7:
         print("contestar")

if llama_hora < 14 and varl_fono !=909:
         print("no contestar")

if llama_hora < 14 and varl_fono ==909:
         print("contestar")

if llama_hora >=17 and llama_hora <=19 and int(varl_fono2)!= 877:
         print("Contestar") 
         
if llama_hora >=17 and llama_hora <=19 and int(varl_fono2)== 877:
         print("no Contestar")            
         
if llama_hora >19:

        print("no contestar")
         
         