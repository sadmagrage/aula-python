masc = []
fem = []
while True:
    print("\033c")
    op = input("Digite M para adicionar uma altura do sexo masculino.\nDigite F para adicionar uma altura do sexo feminino.\nDigite qualquer outro caracter para não adicionar mais valores e realizar a operação.\n")
    if op != "m" and op != "M" and op != "f" and  op != "F":
        break
    altura = float(input("Digite a altura para o sexo selecionado anteriormente.\n"))
    if op == "m" or op == "M":
        masc.append(altura)
    elif op == "f" or op == "F":
        fem.append(altura)
mediamasc = 0
mediafem = 0
if len(masc) >= 1:
    for x in range(len(masc)):
        mediamasc += masc[x]
    else:
        mediamasc/=(x+1)
        print("A altura média masculina é de {:.2f} metros.".format(mediamasc))
if len(fem) >= 1:
    for y in range(len(fem)):
        mediafem += fem[y]
    else:
        mediafem/=(y+1)
        print("A altura média feminina é de {:.2f} metros.".format(mediafem))