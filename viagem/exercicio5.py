def criarLista(oo):
    listnum = oo
    ya = ""
    listanova = []
    x=0
    while x<len(listnum):
        if x == len(listnum)-1:
            ya += listnum[x]
            listanova.append(ya)
        elif listnum[x] == " ":
            listanova.append(ya)
            ya = ""
        elif listnum[x] != " ":
            ya += listnum[x] 
        x+=1
    i = 0
    num = 0
    while i<len(listanova):
        num += float(listanova[i])
        i+=1
    else:
        num/=(i)
    return num
while True:
    op = input("Para achar a média de altura masculina, digite M.\nPara achar a média de altura feminina, digite F.\nPara finalizar a operação, digite qualquer outro caracter.\n")
    if op == "m" or op == "M":
        altm = list(input("Digite as altura masculinas separadas por um espaço, como por exemplo:\n'1.73 1.64 1.80'\n"))
        print("A altura média masculina foi de {:.2f} metros\n".format(criarLista(altm)))
    elif op == "f" or op == "F":
        altf = list(input("Digite as altura femininas separadas por um espaço, como por exemplo:\n'1.73 1.64 1.80'\n"))
        print("A altura média feminina foi de {:.2f} metros\n".format(criarLista(altf)))
    else:
        break