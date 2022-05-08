while True:
    sx = input("Digite o sexo do usuário:\nM para masculino e F para feminino. Para finalizar a instância digite qualquer coisa.\n")
    if sx == "m" or sx == "M":
        h = float(input("Digite a altura :\n"))
        pesoIdeal = (72.7*h) - 58
        print("O peso masculino ideal em relação a altura digitada é {} Kg.".format(pesoIdeal))
    elif sx == "f" or sx == "F":
        h = float(input("Digite a altura :\n"))
        pesoIdeal = (62.1*h) - 44.7
        print("O peso feminino ideal em relação a altura digitada é {} Kg.".format(pesoIdeal))
    else:
        break