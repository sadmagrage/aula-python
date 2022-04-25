import PySimpleGUI as sg
class MyClass:
    def __init__(self,grama,carb,protl,proth,fat):
        self.grama = grama
        self.carb = carb
        self.protl = protl
        self.proth = proth
        self.fat = fat
        self.comida = [self.carb,self.protl,self.proth,self.fat]
        self.lista = [self.comida]
def criar_janela_inicial():
    sg.theme('Black')
    layout = [
    [sg.Text("Leite"),sg.Input("0",key="LeiteGKey",size=(6,1)),sg.Text("Aveia"),sg.Input("0",key="AveiaGKey",size=(6,1)),sg.Text("Banana"),sg.Input("0",key="BananaGKey",size=(6,1)),sg.Text("Peso Total ***"),sg.Input("0",key="pesoTotalKey",size=(6,1)),sg.Text("Velocidade andando ***"),sg.Input("0",key="velKey",size=(6,1))],
    [sg.Text("Ovo"),sg.Input("0",key="OvoGKey",size=(6,1)),sg.Text("Frango"),sg.Input("0",key="FrangoGKey",size=(6,1)),sg.Text("Arroz"),sg.Input("0",key="ArrozGKey",size=(6,1)),sg.Text("Body Fat ***"),sg.Input("0",key="bodyFatKey",size=(6,1)),sg.Text("Minutos andando ***"),sg.Input("0",key="minKey",size=(6,1))],
    [sg.Text("Feijão"),sg.Input("0",key="FeijaoGKey",size=(6,1)),sg.Text("Bife"),sg.Input("0",key="BifeGKey",size=(6,1)),sg.Text("Couve"),sg.Input("0",key="CouveGKey",size=(6,1)),sg.Text("Tempura"),sg.Input("0",key="TempuraGKey",size=(6,1)),sg.Text("Altura ***"),sg.Input("0",key="alturaKey",size=(6,1)),sg.Text("Adicional ***"),sg.Input("0",key="adicionalKey",size=(6,1))],
    [sg.Text("Pastel"),sg.Input("0",key="PastelGKey",size=(6,1)),sg.Text("Ovo Frito"),sg.Input("0",key="OvoFritoGKey",size=(6,1)),sg.Text("Vo2"),sg.Input("0",key="Vo2GKey",size=(6,1)),sg.Text("Udon amarelo"),sg.Input("0",key="UdonAmareloGKey",size=(6,1)),sg.Text("Idade ***"),sg.Input("0",key="idadeKey",size=(6,1)),sg.Text("Ciclo Kcal ***"),sg.Input("0",key="cicloKcalKey",size=(6,1))],
    [sg.Text("Nescau"),sg.Input("0",key="NescauGKey",size=(6,1)),sg.Text("Dona Benta"),sg.Input("0",key="DonaBentaGKey",size=(6,1)),sg.Text("Mussarela"),sg.Input("0",key="MussarelaGKey",size=(6,1)),sg.Text("Molho"),sg.Input("0",key="MolhoGKey",size=(6,1)),sg.Text("Supino ***"),sg.Input("0",key="supinoKey",size=(6,1))],
    [sg.Text("Pão"),sg.Input("0",key="PaoGKey",size=(6,1)),sg.Text("Presunto"),sg.Input("0",key="PresuntoGKey",size=(6,1)),sg.Text("Nesfit Cacau"),sg.Input("0",key="NesfitCacauGKey",size=(6,1)),sg.Text("Whey Growth"),sg.Input("0",key="WheyGrowthGKey",size=(6,1)),sg.Text("Agacho ***"),sg.Input("0",key="agachoKey",size=(6,1))],
    [sg.Text("Miojo"),sg.Input("0",key="MiojoGKey",size=(6,1)),sg.Text("Whopper"),sg.Input("0",key="WhopperGKey",size=(6,1)),sg.Text("Batata"),sg.Input("0",key="BatataGKey",size=(6,1)),sg.Text("Lasanha Swift"),sg.Input("0",key="LasanhaSwiftGKey",size=(6,1)),sg.Text("Terra ***"),sg.Input("0",key="terraKey",size=(6,1))],
    [sg.Text("Suco de Laranja"),sg.Input("0",key="SucoDeLaranjaGKey",size=(6,1)),sg.Text("Poct Poct"),sg.Input("0",key="PoctPoctGKey",size=(6,1)),sg.Text("Supino Choc"),sg.Input("0",key="SupinoChocGKey",size=(6,1)),sg.Text("Cup"),sg.Input("0",key="CupGKey",size=(6,1)),sg.Text("Stiff ***"),sg.Input("0",key="stiffKey",size=(6,1))],
    [sg.Text("Big Crack"),sg.Input("0",key="BigCrackGKey",size=(6,1)),sg.Text("Crisp"),sg.Input("0",key="CrispGKey",size=(6,1)),sg.Text("Udon"),sg.Input("0",key="UdonGKey",size=(6,1)),sg.Text("Teste Prot"),sg.Input("0",key="TesteProtGKey",size=(6,1)),sg.Text("Restante ***"),sg.Input("0",key="restanteKey",size=(6,1))],
    [sg.Text("Teste Carb"),sg.Input("0",key="TesteCarbGKey",size=(6,1))],
    [sg.Button("Bulking"),sg.Button("Cutting"),sg.Text("Déficit Calórico"),sg.Input("0",size=(6,1),key="deficitKey"),sg.Button("Déficit Máximo")],
    [sg.Output(size=(70,10))]
    ]
    return sg.Window('Macros', layout=layout, finalize=True)
def dfctmax():
    pesoTotal = float(values['pesoTotalKey'])
    bodyFat = float(values['bodyFatKey'])
    pesoGordo = pesoTotal*bodyFat
    defctmax = pesoGordo*69.3
    print("O valor máximo recomendado de déficit calórico é:",defctmax)
def bulking():
    pesoTotal = float(values['pesoTotalKey'])
    bodyFat = float(values['bodyFatKey'])
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
    gastoBulk = ((basal+treino+cardio+adicional)*1.3)+cicloKcal
    prothBulkMeta = pesoMagro*2*0.9 #Meta de proteína de alto valor biológico no bulking
    protlBulkMeta = pesoMagro*2*0.1 #Meta de proteína de baixo valor biológico no bulking
    protBulkMeta = prothBulkMeta+protlBulkMeta #Meta de proteína total
    if protl>=protlBulkMeta:
        protl=protlBulkMeta
    if proth>=prothBulkMeta:
        proth=prothBulkMeta
    prot=proth+protl
    kcal = 4*(carb+proth+protl)+fat*9
    resKcal = gastoBulk-kcal
    #Parte confusa
    fatMeta = pesoMagro #Limite de gordura ingerida
    carbBulkMeta = (gastoBulk-(fatMeta*9+protBulkMeta*4))/4 #Meta de carboidratos no bulking
    carbBulkRestante = carbBulkMeta-carb #Quanto falta de carboidrato no bulking
    fatRestante = fatMeta-fat #Quanto falta de gordura
    kcalBulkRestante = gastoBulk-kcal #Quanto falta de kcal no bulking
    prothBulkRestante = prothBulkMeta-proth
    print("Seu peso magro é de : %.2f kg\n"%pesoMagro+"Seu peso gordo é de : %.2f kg\n"%pesoGordo+"O gasto calórico basal é de : %.2f\n"%basal+"O gasto calórico do treino foi de : %.2f kcals\n"%treino+"O consumo calórico no bulking deve ser de : %.2f kcals\n"%gastoBulk+"Até o momento foram consumidos :\n%.2f de carboidrato\n"%carb+"%.2f de proteína total\n"%prot+"%.2f de proteína de baixo valor biológico\n"%protl+"%.2f de proteína de alto valor biológico\n"%proth+"%.2f de gordura\n"%fat+"%.2f de kcals\n"%kcal)
    list1Bulking = [protl,proth,carb,prot,fat,kcal]
    list2Bulking = [protlBulkMeta,prothBulkMeta,carbBulkMeta,protBulkMeta,fatMeta,gastoBulk]
    #CRIAR UMA VARIAVEL ANTES DAS OPERAÇÕES PARA CADA ELIF Q COLOCAR PROTL>PROTLMETA E PROTH>PROTHMET
    xBulk=0
    while xBulk<6:
        if list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==2: #carb            
            print("Está faltando %.2f de carboidrato, no bulking\n"%(list2Bulking[xBulk]-list1Bulking[xBulk])+"Sugestão de carbo:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format((carbBulkRestante/lista[6].carb),(carbBulkRestante/lista[34].carb),(carbBulkRestante/lista[2].carb),(carbBulkRestante/lista[4].carb))+"\n")
            if list2Bulking[4]<list1Bulking[4]:
                pass
            else:
                print("\nSugestão de carbo ENGLOBANDO A GORDURA:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format(((carbBulkRestante+(fatRestante*9/4))/lista[6].carb),((carbBulkRestante+(fatRestante*9/4))/lista[34].carb),((carbBulkRestante+(fatRestante*9/4))/lista[2].carb),((carbBulkRestante+(fatRestante*9/4))/lista[4].carb)))
        elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==3: #prot total
            print("Está faltando %.2f de proteína total, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
        elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==0: #prot low
            print("Está faltando %.2f de proteína de baixo valor biológico, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
        elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==1: #prot high
            print("Está faltando %.2f de proteína de alto valor biológico, no bulking\n"%(list2Bulking[xBulk]-list1Bulking[xBulk])+"Sugestão de proteína de alto valor biológico:\n{:.2f} gramas de frango\n{:.2f} gramas de testeprot\n{:.2f}gramas de bife\n{:.2f}gramas de wgrowth\n{:.2f}gramas de ovo cozido\n{:.2f}gramas de ovo frito\n{:.2f}gramas de leite".format((prothBulkRestante/lista[5].proth),(prothBulkRestante/lista[33].proth),(prothBulkRestante/lista[8].proth),(prothBulkRestante/lista[22].proth),(prothBulkRestante/lista[3].proth),(prothBulkRestante/lista[12].proth),(prothBulkRestante/lista[0].proth)))
        elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==4: #fat
            print("Está faltando %.2f de gordura, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
        elif xBulk==5 and gastoBulk>kcal:
            print("Está faltando %.2f de kcals, no bulking"%(resKcal))
        elif xBulk==5 and gastoBulk<=kcal:
            print("Passaram %.2f de kcals, no bulking"%(-resKcal))
        xBulk+=1
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
            print("Está faltando %.2f de carboidrato, no cutting\n"%(list2Cutting[xCut]-list1Cutting[xCut])+"Sugestão de carbo:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format((carbCutRestante/lista[6].carb),(carbCutRestante/lista[34].carb),(carbCutRestante/lista[2].carb),(carbCutRestante/lista[4].carb))+"\n")
            if list2Cutting[4]<list1Cutting[4]:
                pass
            else:
                print("Sugestão de carbo ENGLOBANDO A GORDURA:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format(((carbCutRestante+(fatRestante*9/4))/lista[6].carb),((carbCutRestante+(fatRestante*9/4))/lista[34].carb),((carbCutRestante+(fatRestante*9/4))/lista[2].carb),((carbCutRestante+(fatRestante*9/4))/lista[4].carb)))
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
janela = criar_janela_inicial()
while True:
    event, values = janela.read()
    if event=='Déficit Máximo':
        dfctmax()
    elif event=='Bulking':
        bulking()
    elif event=='Cutting':
        cutting()
    elif event==sg.WIN_CLOSED:
        break