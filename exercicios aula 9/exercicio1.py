carneirinho = 0
while True:
    dormiu = input("Já dormiu ? s/n\n")
    if dormiu == "s" or dormiu == "S":
        print("Dormiu após contar {} carneirinhos.".format(carneirinho))
        break
    elif dormiu == "n" or dormiu == "N":
        carneirinho+=1
    else:
        print("Resposta inválida.")
        break