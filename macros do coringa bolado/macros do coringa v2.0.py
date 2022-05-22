import PySimpleGUI as sg
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb['comida']
x = mycol.find()
list1 = list(x)
list2 = []
newLayout = [[],
    [sg.Text("Peso Total ***"),sg.Input("0",key="pesoTotalKey",size=(6,1)),sg.Text("Body Fat ***"),sg.Input("0",key="bodyFatKey",size=(6,1)),sg.Text("Altura ***"),sg.Input("0",key="alturaKey",size=(6,1)),sg.Text("Idade ***"),sg.Input("0",key="idadeKey",size=(6,1)),sg.Text("Velocidade ***"),sg.Input("0",key="velKey",size=(6,1)),sg.Text("Minutos ***"),sg.Input("0",key="minKey",size=(6,1))],
    [sg.Text("Supino ***"),sg.Input("0",key="supinoKey",size=(6,1)),sg.Text("Agacho ***"),sg.Input("0",key="agachoKey",size=(6,1)),sg.Text("Terra ***"),sg.Input("0",key="terraKey",size=(6,1)),sg.Text("Stiff ***"),sg.Input("0",key="stiffKey",size=(6,1)),sg.Text("Restante ***"),sg.Input("0",key="restanteKey",size=(6,1)),sg.Text("Adicional ***"),sg.Input("0",key="adicionalKey",size=(6,1))],
    [sg.Text("Ciclo Kcal ***"),sg.Input("0",key="cicloKcalKey",size=(6,1))],
    [sg.Button("Bulking"),sg.Button("Cutting"),sg.Text("Superávit Calórico em %"),sg.Input("0",size=(6,1),key="superavitKey"),sg.Text("Déficit Calórico"),sg.Input("0",size=(6,1),key="deficitKey"),sg.Button("Déficit Máximo")],
    [sg.Output(size=(70,10))]
    ]
for y in range(len(list1)):
    if len(newLayout[-6])==12:
        newLayout.insert(-5,[])
        newLayout[-6].append(sg.Text(list1[y].get("name")))
        newLayout[-6].append(sg.Input("0",key=list1[y].get("key"), size=(6,1)))
    else:
        newLayout[-6].append(sg.Text(list1[y].get("name")))
        newLayout[-6].append(sg.Input("0",key=list1[y].get("key"), size=(6,1)))
def criar_janela_inicial():
    sg.theme('Black')
    layout = newLayout
    return sg.Window('Macros', layout=layout, finalize=True)
class MyClass:
    def __init__(self,grama,carb,protl,proth,fat):
        self.grama = grama
        self.carb = carb
        self.protl = protl
        self.proth = proth
        self.fat = fat
        self.comida = [self.carb,self.protl,self.proth,self.fat]
        self.lista = [self.comida]
def dfctmax():
    pesoTotal = float(values['pesoTotalKey'])
    bodyFat = float(values['bodyFatKey'])
    pesoGordo = pesoTotal*bodyFat
    defctmax = pesoGordo*69.3
    print("O valor máximo recomendado de déficit calórico é:",defctmax)
def bulking():
    list3 = []
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
    superavit = float(values['superavitKey'])/100
    pesoGordo = pesoTotal*bodyFat
    pesoMagro = pesoTotal-pesoGordo
    harrisBennedictMale = 66.5+(13.75*pesoMagro)+(5.003*altura)-(6.755*idade)
    if pesoTotal==0:
        harrisBennedictMale=0
    basal = harrisBennedictMale*1.3
    indice = pesoMagro*90*0.1
    treino = (1.25*supino*indice/34)+(1.5*terra*indice/34)+(2*agacho*indice/34)+(1.5*stiff*indice/34)+(restante*indice/34)
    cardio = 0.0175*pesoMagro*vel*minutos
    gastoBulk = ((basal+treino+cardio+adicional)*(1+superavit))+cicloKcal
    for i in range(len(list1)):
        list2.append(list1[i].get("key"))
    for u in range (len(list2)):
        list3.append(float(values[list2[u]]))
    carb = 0
    protl = 0
    proth = 0
    fat = 0
    lista = ["carb","protl","proth","fat"]
    for a in range(len(list1)):
        for k in range(len(lista)):
            if k==0:
                carb += list3[a]*eval(list1[a].get(lista[k]))
            elif k==1:
                protl += list3[a]*eval(list1[a].get(lista[k]))
            elif k==2:
                proth += list3[a]*eval(list1[a].get(lista[k]))
            elif k==3:
                fat += list3[a]*eval(list1[a].get(lista[k]))
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
    print("\n\n\n\nSeu peso magro é de : {:.2f} kg\nSeu peso gordo é de : {:.2f} kg\nO gasto calórico basal é de : {:.2f}\nO gasto calórico do treino foi de : {:.2f} kcals\nO consumo calórico no bulking deve ser de : {:.2f} kcals\nAté o momento foram consumidos :\n{:.2f} de carboidrato\n{:.2f} de proteína total\n{:.2f} de proteína de baixo valor biológico\n{:.2f} de proteína de alto valor biológico\n{:.2f} de gordura\n{:.2f} de kcals\n".format(pesoMagro,pesoGordo,basal,treino,gastoBulk,carb,prot,protl,proth,fat,kcal))
    list1Bulking = [protl,proth,carb,prot,fat,kcal]
    list2Bulking = [protlBulkMeta,prothBulkMeta,carbBulkMeta,protBulkMeta,fatMeta,gastoBulk]
    #CRIAR UMA VARIAVEL ANTES DAS OPERAÇÕES PARA CADA ELIF Q COLOCAR PROTL>PROTLMETA E PROTH>PROTHMET
    xBulk=0
    while xBulk<6:
        if list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==2: #carb            
            print("Está faltando %.2f de carboidrato, no bulking\n"%(list2Bulking[xBulk]-list1Bulking[xBulk])+"Sugestão de carbo:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format((carbBulkRestante/eval(list1[6].get("carb"))),(carbBulkRestante/eval(list1[34].get("carb"))),(carbBulkRestante/eval(list1[2].get("carb"))),(carbBulkRestante/eval(list1[4].get("carb"))))+"\n")
            if list2Bulking[4]<list1Bulking[4]:
                pass
            else:
                print("\nSugestão de carbo ENGLOBANDO A GORDURA:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format(((carbBulkRestante+(fatRestante*9/4))/eval(list1[6].get("carb"))),((carbBulkRestante+(fatRestante*9/4))/eval(list1[34].get("carb"))),((carbBulkRestante+(fatRestante*9/4))/eval(list1[2].get("carb"))),((carbBulkRestante+(fatRestante*9/4))/eval(list1[4].get("carb")))))
        elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==3: #prot total
            print("Está faltando %.2f de proteína total, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
        elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==0: #prot low
            print("Está faltando %.2f de proteína de baixo valor biológico, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
        elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==1: #prot high
            print("Está faltando %.2f de proteína de alto valor biológico, no bulking\n"%(list2Bulking[xBulk]-list1Bulking[xBulk])+"Sugestão de proteína de alto valor biológico:\n{:.2f} gramas de frango\n{:.2f} gramas de testeprot\n{:.2f}gramas de bife\n{:.2f}gramas de wgrowth\n{:.2f}gramas de ovo cozido\n{:.2f}gramas de ovo frito\n{:.2f}gramas de leite".format((prothBulkRestante/eval(list1[5].get("proth"))),(prothBulkRestante/eval(list1[33].get("proth"))),(prothBulkRestante/eval(list1[8].get("proth"))),(prothBulkRestante/eval(list1[22].get("proth"))),(prothBulkRestante/eval(list1[3].get("proth"))),(prothBulkRestante/eval(list1[12].get("proth"))),(prothBulkRestante/eval(list1[5].get("proth")))))
        elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==4: #fat
            print("Está faltando %.2f de gordura, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
        elif xBulk==5 and gastoBulk>kcal:
            print("Está faltando %.2f de kcals, no bulking"%(resKcal))
        elif xBulk==5 and gastoBulk<=kcal:
            print("Passaram %.2f de kcals, no bulking"%(-resKcal))
        xBulk+=1
    del list3
def cutting():
    list3 = []
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
    for i in range(len(list1)):
        list2.append(list1[i].get("key"))
    for u in range (len(list2)):
        list3.append(float(values[list2[u]]))
    carb = 0
    protl = 0
    proth = 0
    fat = 0
    lista = ["carb","protl","proth","fat"]
    for a in range(len(list1)):
        for k in range(len(lista)):
            if k==0:
                carb += list3[a]*eval(list1[a].get(lista[k]))
            elif k==1:
                protl += list3[a]*eval(list1[a].get(lista[k]))
            elif k==2:
                proth += list3[a]*eval(list1[a].get(lista[k]))
            elif k==3:
                fat += list3[a]*eval(list1[a].get(lista[k]))
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
    print("\n\n\n\nSeu peso magro é de : {:.2f} kg\nSeu peso gordo é de : {:.2f} kg\nO gasto calórico basal é de : {:.2f}\nO gasto calórico do treino foi de : {:.2f} kcals\nO consumo calórico no cutting deve ser de : {:.2f} kcals\nAté o momento foram consumidos :\n{:.2f} de carboidrato\n{:.2f} de proteína total\n{:.2f} de proteína de baixo valor biológico\n{:.2f} de proteína de alto valor biológico\n{:.2f} de gordura\n{:.2f} de kcals\n".format(pesoMagro,pesoGordo,basal,treino,gastoCut,carb,prot,protl,proth,fat,kcal))
    list1Cutting = [protl,proth,carb,prot,fat,kcal]
    list2Cutting = [protlCutMeta,prothCutMeta,carbCutMeta,protCutMeta,fatMeta,gastoCut]
    #CRIAR UMA VARIAVEL ANTES DAS OPERAÇÕES PARA CADA ELIF Q COLOCAR PROTL>PROTLMETA E PROTH>PROTHMET
    xCut=0
    while xCut<6:
        if list2Cutting[xCut]>list1Cutting[xCut] and xCut==2: #carb
            print("Está faltando %.2f de carboidrato, no cutting\n"%(list2Cutting[xCut]-list1Cutting[xCut])+"Sugestão de carbo:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format((carbCutRestante/eval(list1[6].get("carb"))),(carbCutRestante/eval(list1[34].get("carb"))),(carbCutRestante/eval(list1[2].get("carb"))),(carbCutRestante/eval(list1[4].get("carb"))))+"\n")
            if list2Cutting[4]<list1Cutting[4]:
                pass
            else:
                print("Sugestão de carbo ENGLOBANDO A GORDURA:\n{:.2f} gramas de arroz\n{:.2f} gramas de testecarb\n{:.2f}gramas de udon\n{:.2f} gramas de banana".format(((carbCutRestante+(fatRestante*9/4))/eval(list1[6].get("carb"))),((carbCutRestante+(fatRestante*9/4))/eval(list1[34].get("carb"))),((carbCutRestante+(fatRestante*9/4))/eval(list1[2].get("carb"))),((carbCutRestante+(fatRestante*9/4))/eval(list1[4].get("carb")))))
        elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==3: #prot total
            print("Está faltando %.2f de proteína total, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
        elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==0: #prot low
            print("Está faltando %.2f de proteína de baixo valor biológico, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
        elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==1: #prot high
            print("Está faltando %.2f de proteína de alto valor biológico, no cuutting\n"%(list2Cutting[xCut]-list1Cutting[xCut])+"Sugestão de proteína de alto valor biológico:\n{:.2f} gramas de frango\n{:.2f} gramas de testeprot\n{:.2f}gramas de bife\n{:.2f}gramas de wgrowth\n{:.2f}gramas de ovo cozido\n{:.2f}gramas de ovo frito\n{:.2f}gramas de leite".format((prothCutRestante/eval(list1[5].get("proth"))),(prothCutRestante/eval(list1[33].get("proth"))),(prothCutRestante/eval(list1[8].get("proth"))),(prothCutRestante/eval(list1[22].get("proth"))),(prothCutRestante/eval(list1[3].get("proth"))),(prothCutRestante/eval(list1[12].get("proth"))),(prothCutRestante/eval(list1[0].get("proth")))))
        elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==4: #fat
            print("Está faltando %.2f de gordura, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
        elif xCut==5 and gastoCut>kcal:
            print("Está faltando %.2f de kcals, no cutting"%(resKcal))
        elif xCut==5 and gastoCut<=kcal:
            print("Passaram %.2f de kcals, no cutting"%(-resKcal))
        xCut+=1
    del list3
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