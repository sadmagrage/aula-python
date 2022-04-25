class MyClass:
    def __init__(self,grama,carb,protl,proth,fat):
        self.grama = grama
        self.carb = carb
        self.protl = protl
        self.proth = proth
        self.fat = fat
        self.comida = [self.carb,self.protl,self.proth,self.fat]
        self.lista = [self.comida]
#       DADOS PESSOAIS
#
#
#
pesoTotal = 83.9
bodyFat = 0.1
altura = 173
idade = 18
supino = 0
agacho = 0
terra = 0
stiff = 0
restante = 0
vel = 0
min = 0
adicional = 0
cicloKcal = 0.0
#       GRAMA DOS ALIMENTOS
#
#
leiteg = 0
aveiag = 0
udong = 0
ovog = 0
bananag = 0
frangog = 0
arrozg = 0
feijaog = 0
bifeg = 0
couveg = 0
tempurag = 0
pastelg = 0
ovofritog = 0
vo2g = 0
udonamarelog = 0
nescaug = 0
donabentag = 0
mussarelag = 0
molhog = 0
paog = 0
presuntog = 0
nesfitcacaug = 0
wgrowthg = 0
miojog = 0
whopperg = 0
batatag = 0
lasanhaswiftg = 0
sucodelaranjag = 0
poctpoctg = 0
supinochocg = 0
cupg = 0
bigcrackg = 0
crispg = 0
testeprotg = 1
testecarbg = 300
#
#
#
leite = MyClass(leiteg,0.0452,0,0.0322,0.0325)
aveia = MyClass(aveiag,1.7/3,4.8/30,0,1.8/30)
udon = MyClass(udong,5.9/8.0, 8.3/80, 0, 0.8/80)
ovo = MyClass(ovog,0.56/50,0,6.26/50,5.28/50)
banana = MyClass(bananag,22.84/100,1.09/100,0,0.33/100)
frango = MyClass(frangog,0, 0, 31.02/100, 3.57/100)
arroz = MyClass(arrozg,28.59/100,2.38/100, 0, 0.21/100)
feijao = MyClass(feijaog,13.61/100,5.04/100,0,0.85/100)
bife = MyClass(bifeg,0,0,27.29/100,15.01/100)
couve = MyClass(couveg,10.01/100,3.3/100,0,0.7/100)
tempura = MyClass(tempurag,13.78/100,4.23/100,0,10.09/100)
pastel = MyClass(pastelg,0.438,10.1/100,0,18.3/100)
ovofrito = MyClass(ovofritog,0.43/46,0,6.24/46,6.76/46)
vo2 = MyClass(vo2g,13,0,9,3.4)
udonamarelo = MyClass(udonamarelog,5.9/8.0, 8.4/80,0,0.8/80)
nescau = MyClass(nescaug,1.7/2.0,0.7/20,0,0)
donabenta = MyClass(donabentag,5.4/8.0,6.6/80,0,1.1/80)
mussarela = MyClass(mussarelag,0,0,38.0/100,17.0/100)
molho = MyClass(molhog,5.62/100,1.14/100,0,2.47/100)
pao = MyClass(paog,58.6/100,8.0/100,0,3.10/100)
presunto = MyClass(presuntog,0,13.25/100,0,6.75/100)
nesfitcacau = MyClass(nesfitcacaug,20.0/30,2.3/30,0,4.9/30)
wgrowth = MyClass(wgrowthg,4.0/30,0,23.0/30,1.6/30)
miojo = MyClass(miojog,49.0,8.5,0,16.0)
whopper = MyClass(whopperg,54.0,18.5,18.5,35.0)
batata = MyClass(batatag,20.01/100,1.71/100,0,0.1/100)
lasanhaswift = MyClass(lasanhaswiftg,55.0/300,19.0/300,0,11.0/300)
sucodelaranja = MyClass(sucodelaranjag,20.0/200,1.4/200,0,0)
poctpoct = MyClass(poctpoctg,34.0,20.0,0,12.0)
supinochoc = MyClass(supinochocg,12.0,0,10.0,2.7)
cup = MyClass(cupg,43.0,7.5,0,12.0)
bigcrack = MyClass(bigcrackg,41.0,26.0,0,26.0)
crisp = MyClass(crispg,18.0,0,13.0,7.3)
testeprot = MyClass(testeprotg,0,15.11,135.93,0)
testecarb = MyClass(testecarbg,30/30,0,0,0)
lista = [leite, aveia, udon, ovo, banana, frango, arroz, feijao, bife, couve, tempura, pastel, ovofrito, vo2,udonamarelo, nescau, donabenta, mussarela, molho, pao, presunto, nesfitcacau, wgrowth, miojo, whopper, batata, lasanhaswift, sucodelaranja, poctpoct, supinochoc, cup, bigcrack, crisp, testeprot, testecarb]
#
#
#
i=0
carb = 0
prot = 0
protl = 0
proth = 0
fat = 0
while i<(len(lista)):
    carb+=lista[i].carb*lista[i].grama
    protl+=lista[i].protl*lista[i].grama
    proth+=lista[i].proth*lista[i].grama
    prot+=lista[i].protl*lista[i].grama+lista[i].proth*lista[i].grama
    fat+=lista[i].fat*lista[i].grama
    i+=1
kcal = 4*(carb+prot)+fat*9
pesoGordo = pesoTotal*bodyFat
pesoMagro = pesoTotal-pesoGordo
harrisBennedictMale = 66.5+(13.75*pesoMagro)+(5.003*altura)-(6.755*idade)
basal = harrisBennedictMale*1.3
indice = pesoMagro*90*0.1
treino = (1.25*supino*indice/34)+(1.5*terra*indice/34)+(2*agacho*indice/34)+(1.5*stiff*indice/34)+(restante*indice/34)
cardio = 0.0175*pesoMagro*vel*min
gastoBulk = ((basal+treino+cardio+adicional)*1.3)+cicloKcal
gastoCut = (basal+treino+cardio+adicional+cicloKcal)-(pesoGordo*69.3)
#Parte confusa
prothBulkMeta = pesoMagro*2*0.9 #Meta de proteína de alto valor biológico no bulking
protlBulkMeta = pesoMagro*2*0.1 #Meta de proteína de baixo valor biológico no bulking
protBulkMeta = prothBulkMeta+protlBulkMeta #Meta de proteína total
prothCutMeta = pesoMagro*3*0.9 #Meta de proteína de alto valor biológico no cutting
protlCutMeta = pesoMagro*3*0.1 #Meta de proteína de baixo valor biológico no cutting
protCutMeta = prothCutMeta+protlCutMeta #Meta de proteína total
fatMeta = pesoMagro #Limite de gordura ingerida
carbBulkMeta = (gastoBulk-(fatMeta*9+protBulkMeta*4))/4 #Meta de carboidratos no bulking
carbCutMeta = (gastoCut-(fatMeta*9+protCutMeta*4))/4 #Meta de carboidratos no cutting
carbBulkRestante = carbBulkMeta-carb #Quanto falta de carboidrato no bulking
carbCutRestante = carbCutMeta-carb #Quanto falta de carboidrato no cutting
protBulkRestante = protBulkMeta-prot #Quanto falta de proteína no bulking
protCutRestante = protCutMeta-prot #Quanto falta de proteína no cutting
protlBulkRestante = protlBulkMeta-protl #Quanto falta de proteína de baixo valor biológico no bulking
protlCutRestante = protlBulkMeta-protl #Quanto falta de proteína de baixo valor biológico no cutting
prothBulkRestante = prothBulkMeta-proth #Quanto falta de proteína de alto valor biológico no bulking
prothCutRestante = prothBulkMeta-proth #Quanto falta de proteína de alto valor biológico no cutting
fatRestante = fatMeta-fat #Quanto falta de gordura
kcalBulkRestante = gastoBulk-kcal #Quanto falta de kcal no bulking
kcalCutRestante = gastoCut-kcal #Quanto falta de kcal no cutting
print("Seu peso magro é de : %.2f kg\n"%pesoMagro+"Seu peso gordo é de : %.2f kg\n"%pesoGordo+"O gasto calórico basal é de : %.2f\n"%basal+"O gasto calórico do treino foi de : %.2f kcals\n"%treino+"O consumo calórico no bulking deve ser de : %.2f kcals\n"%gastoBulk+"O consumo calórico mínimo no cutting deve ser : %.2f kcals\n"%gastoCut+"Até o momento foram consumidos :\n%.2f de carboidrato\n"%carb+"%.2f de proteína total\n"%prot+"%.2f de proteína de baixo valor biológico\n"%protl+"%.2f de proteína de alto valor biológico\n"%proth+"%.2f de gordura\n"%fat+"%.2f de kcals\n"%kcal)
list1Bulking = [carb,prot,protl,proth,fat,kcal]
list2Bulking = [carbBulkMeta,protBulkMeta,protlBulkMeta,prothBulkMeta,fatMeta,gastoBulk]
xBulk=0
list1Cutting = [carb,prot,protl,proth,fat,kcal]
list2Cutting = [carbCutMeta,protCutMeta,protlCutMeta,prothCutMeta,fatMeta,gastoCut]
xCut=0
while xBulk<6:
    if list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==0:
        print("\nEstá faltando %.2f de carboidrato, no bulking\n"%(list2Bulking[xBulk]-list1Bulking[xBulk])+"Sugestão de carbo ENGLOBANDO A GORDURA:\n{} gramas de arroz\n{} gramas de testecarb".format(((carbBulkRestante+(fatRestante*9/4))/lista[6].carb),((carbBulkRestante+(fatRestante*9/4))/lista[34].carb)))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==1:
        print("Está faltando %.2f de proteína total, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==2:
        print("Está faltando %.2f de proteína de baixo valor biológico, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==3:
        print("Está faltando %.2f de proteína de alto valor biológico, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==4:
        print("Está faltando %.2f de gordura, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==5:
        print("Está faltando %.2f de kcal, no bulking\n"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
    xBulk+=1
while xCut<6:
    if list2Cutting[xCut]>list1Cutting[xCut] and xCut==0:
        print("\nEstá faltando %.2f de carboidrato, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==1:
        print("Está faltando %.2f de proteína total, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==2:
        print("Está faltando %.2f de proteína de baixo valor biológico, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==3:
        print("Está faltando %.2f de proteína de alto valor biológico, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==4:
        print("Está faltando %.2f de gordura, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==5:
        print("Está faltando %.2f de kcal, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    xCut+=1