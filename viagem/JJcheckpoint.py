def cutting():
    pesoTotal = float(values['pesoTotalKey'])
    bodyFat = float(values['bodyFatKey'])
    deficit = float(values['deficitKey'])
    vel = float(values['velKey'])
    minutos = float(values['minKey'])
    altura = float(values['alturaKey'])
    idade = float(values['idadeKey'])
    supino = int(values['supinoKey'])
    agacho = int(values['agachoKey'])
    terra = int(values['terraKey'])
    stiff = int(values['stiffKey'])
    restante = int(values['restanteKey'])
    adicional = float(values['adicionalKey'])
    cicloKcal = float(values['cicloKcalKey'])
    leite = MyClass(float(values['LeiteGKey']),0.0452,0,0.0322,0.0325)
    aveia = MyClass(float(values['AveiaGKey']),1.7/3,4.8/30,0,1.8/30)
    udon = MyClass(float(values['UdonGKey']),5.9/8.0, 8.3/80, 0, 0.8/80)
    ovo = MyClass(float(values['OvoGKey']),0.56/50,0,6.26/50,5.28/50)
    banana = MyClass(float(values['BananaGKey']),22.84/100,1.09/100,0,0.33/100)
    frango = MyClass(float(values['FrangoGKey']),0, 0, 31.02/100, 3.57/100)
    arroz = MyClass(float(values['ArrozGKey']),28.59/100,2.38/100, 0, 0.21/100)
    feijao = MyClass(float(values['FeijaoGKey']),13.61/100,5.04/100,0,0.85/100)
    bife = MyClass(float(values['BifeGKey']),0,0,27.29/100,15.01/100)
    couve = MyClass(float(values['CouveGKey']),10.01/100,3.3/100,0,0.7/100)
    tempura = MyClass(float(values['TempuraGKey']),13.78/100,4.23/100,0,10.09/100)
    pastel = MyClass(float(values['PastelGKey']),0.438,10.1/100,0,18.3/100)
    ovofrito = MyClass(float(values['OvoFritoGKey']),0.43/46,0,6.24/46,6.76/46)
    vo2 = MyClass(float(values['Vo2GKey']),13,0,9,3.4)
    udonamarelo = MyClass(float(values['UdonAmareloGKey']),5.9/8.0, 8.4/80,0,0.8/80)
    nescau = MyClass(float(values['NescauGKey']),1.7/2.0,0.7/20,0,0)
    donabenta = MyClass(float(values['DonaBentaGKey']),5.4/8.0,6.6/80,0,1.1/80)
    mussarela = MyClass(float(values['MussarelaGKey']),0,0,38.0/100,17.0/100)
    molho = MyClass(float(values['MolhoGKey']),5.62/100,1.14/100,0,2.47/100)
    pao = MyClass(float(values['PaoGKey']),58.6/100,8.0/100,0,3.10/100)
    presunto = MyClass(float(values['PresuntoGKey']),0,13.25/100,0,6.75/100)
    nesfitcacau = MyClass(float(values['NesfitCacauGKey']),20.0/30,2.3/30,0,4.9/30)
    wgrowth = MyClass(float(values['WheyGrowthGKey']),4.0/30,0,23.0/30,1.6/30)
    miojo = MyClass(float(values['MiojoGKey']),49.0,8.5,0,16.0)
    whopper = MyClass(float(values['WhopperGKey']),54.0,18.5,18.5,35.0)
    batata = MyClass(float(values['BatataGKey']),20.01/100,1.71/100,0,0.1/100)
    lasanhaswift = MyClass(float(values['LasanhaSwiftGKey']),55.0/300,19.0/300,0,11.0/300)
    sucodelaranja = MyClass(float(values['SucoDeLaranjaGKey']),20.0/200,1.4/200,0,0)
    poctpoct = MyClass(float(values['PoctPoctGKey']),34.0,20.0,0,12.0)
    supinochoc = MyClass(float(values['SupinoChocGKey']),12.0,0,10.0,2.7)
    cup = MyClass(float(values['CupGKey']),43.0,7.5,0,12.0)
    bigcrack = MyClass(float(values['BigCrackGKey']),41.0,26.0,0,26.0)
    crisp = MyClass(float(values['CrispGKey']),18.0,0,13.0,7.3)
    testeprot = MyClass(float(values['TesteProtGKey']),0,23.19,208.74,0)
    testecarb = MyClass(float(values['TesteCarbGKey']),30/30,0,0,0)
    lista = [leite, aveia, udon, ovo, banana, frango, arroz, feijao, bife, couve, tempura, pastel, ovofrito, vo2,udonamarelo, nescau, donabenta, mussarela, molho, pao, presunto, nesfitcacau, wgrowth, miojo, whopper, batata, lasanhaswift, sucodelaranja, poctpoct, supinochoc, cup, bigcrack, crisp, testeprot, testecarb]
    #
    #
    #
    i=0
    carb = 0
    protl = 0
    proth = 0
    prot = 0
    fat = 0
    while i<(len(lista)):
        carb+=lista[i].carb*lista[i].grama
        protl+=lista[i].protl*lista[i].grama
        proth+=lista[i].proth*lista[i].grama
        fat+=lista[i].fat*lista[i].grama
        i+=1
    pesoGordo = pesoTotal*bodyFat
    pesoMagro = pesoTotal-pesoGordo
    harrisBennedictMale = 66.5+(13.75*pesoMagro)+(5.003*altura)-(6.755*idade)
    if pesoTotal==0:
        harrisBennedictMale=0
    basal = harrisBennedictMale*1.3
    indice = pesoMagro*90*0.1
    treino = (1.25*supino*indice/34)+(1.5*terra*indice/34)+(2*agacho*indice/34)+(1.5*stiff*indice/34)+(restante*indice/34)
    cardio = 0.0175*pesoMagro*vel*minutos
    deficitmax = pesoGordo*69.3
    gastoCut = basal+treino+cardio+adicional+cicloKcal-deficit
    prothCutMeta = pesoMagro*3*0.9 #Meta de proteína de alto valor biológico no Cutting
    protlCutMeta = pesoMagro*3*0.1 #Meta de proteína de baixo valor biológico no Cutting
    protCutMeta = prothCutMeta+protlCutMeta #Meta de proteína total
    if protl>=protlCutMeta:
        protl=protlCutMeta
    if proth>=prothCutMeta:
        proth=prothCutMeta
    prot=proth+protl
    kcal = 4*(carb+proth+protl)+fat*9
    resKcal = gastoCut-kcal
    #Parte confusa
    fatMeta = pesoMagro #Limite de gordura ingerida
    carbCutMeta = (gastoCut-(fatMeta*9+protCutMeta*4))/4 #Meta de carboidratos no cutting
    carbCutRestante = carbCutMeta-carb #Quanto falta de carboidrato no cutting
    fatRestante = fatMeta-fat #Quanto falta de gordura
    kcalCutRestante = gastoCut-kcal #Quanto falta de kcal no cutting
    prothCutRestante = prothCutMeta-proth
    print("Seu peso magro é de : %.2f kg\n"%pesoMagro+"Seu peso gordo é de : %.2f kg\n"%pesoGordo+"O gasto calórico basal é de : %.2f\n"%basal+"O gasto calórico do treino foi de : %.2f kcals\n"%treino+"O consumo calórico no cutting deve ser de : %.2f kcals\n"%gastoCut+"Até o momento foram consumidos :\n%.2f de carboidrato\n"%carb+"%.2f de proteína total\n"%prot+"%.2f de proteína de baixo valor biológico\n"%protl+"%.2f de proteína de alto valor biológico\n"%proth+"%.2f de gordura\n"%fat+"%.2f de kcals\n"%kcal)
    list1Cutting = [protl,proth,carb,prot,fat,kcal]
    list2Cutting = [protlCutMeta,prothCutMeta,carbCutMeta,protCutMeta,fatMeta,gastoCut]
    #CRIAR UMA VARIAVEL ANTES DAS OPERAÇÕES PARA CADA ELIF Q COLOCAR PROTL>PROTLMETA E PROTH>PROTHMET
    xCut=0
    while xCut<6:
        if list2Cutting[xCut]>list1Cutting[xCut] and xCut==2: #carb
            print("Está faltando %.2f de carboidrato, no cutting\n"%(list2Cutting[xCut]-list1Cutting[xCut])+"Sugestão de carbo:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format((carbCutRestante/lista[6].carb),(carbCutRestante/lista[34].carb),(carbCutRestante/lista[2].carb),(carbCutRestante/lista[4].carb))+"\nSugestão de carbo ENGLOBANDO A GORDURA:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format(((carbCutRestante+(fatRestante*9/4))/lista[6].carb),((carbCutRestante+(fatRestante*9/4))/lista[34].carb),((carbCutRestante+(fatRestante*9/4))/lista[2].carb),((carbCutRestante+(fatRestante*9/4))/lista[4].carb)))
        elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==3: #prot total
            print("Está faltando %.2f de proteína total, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
        elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==0: #prot low
            print("Está faltando %.2f de proteína de baixo valor biológico, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
        elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==1: #prot high
            print("Está faltando %.2f de proteína de alto valor biológico, no cuutting\n"%(list2Cutting[xCut]-list1Cutting[xCut])+"Sugestão de proteína de alto valor biológico:\n{:.2f} gramas de frango\n{:.2f} gramas de testeprot\n{:.2f}gramas de bife\n{:.2f}gramas de wgrowth\n{:.2f}gramas de ovo cozido\n{:.2f}gramas de ovo frito\n{:.2f}gramas de leite".format((prothCutRestante/lista[5].proth),(prothCutRestante/lista[33].proth),(prothCutRestante/lista[8].proth),(prothCutRestante/lista[22].proth),(prothCutRestante/lista[3].proth),(prothCutRestante/lista[12].proth),(prothCutRestante/lista[0].proth)))
        elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==4: #fat
            print("Está faltando %.2f de gordura, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
        elif xCut==5 and gastoCut>kcal:
            print("Está faltando %.2f de kcals, no cutting"%(resKcal))
        elif xCut==5 and gastoCut<=kcal:
            print("Passaram %.2f de kcals, no cutting"%(-resKcal))
        xCut+=1