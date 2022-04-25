
##
list1Bulking = [protl,proth,carb,prot,fat,kcal]
list2Bulking = [protlBulkMeta,prothBulkMeta,carbBulkMeta,protBulkMeta,fatMeta,gastoBulk]
#CRIAR UMA VARIAVEL ANTES DAS OPERAÇÕES PARA CADA ELIF Q COLOCAR PROTL>PROTLMETA E PROTH>PROTHMET
xBulk=0
kcalBulkPROTLproth = kcal-(protlresto*4)
kcalBulkprotlPROTH = kcal-(prothresto*4)
kcalBulkPROTLPROTH = kcal-((protlresto*4)+(prothresto*4))
list1Cutting = [protl,proth,carb,prot,fat,kcal]
list2Cutting = [protlCutMeta,prothCutMeta,carbCutMeta,protCutMeta,fatMeta,gastoCut]
xCut=0
while xBulk<6:
    if list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==2: #carb
        print("\nEstá faltando %.2f de carboidrato, no bulking\n"%(list2Bulking[xBulk]-list1Bulking[xBulk])+"Sugestão de carbo ENGLOBANDO A GORDURA:\n{} gramas de arroz\n{} gramas de testecarb".format(((carbBulkRestante+(fatRestante*9/4))/lista[6].carb),((carbBulkRestante+(fatRestante*9/4))/lista[34].carb)))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==3: #prot total
        print("Está faltando %.2f de proteína total, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==0: #prot low
        print("Está faltando %.2f de proteína de baixo valor biológico, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==1: #prot high
        print("Está faltando %.2f de proteína de alto valor biológico, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==4: #fat
        print("Está faltando %.2f de gordura, no bulking"%(list2Bulking[xBulk]-list1Bulking[xBulk]))
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==5: #kcal #um das quatro condições
        print("Está faltando %.2f de kcal, no bulking\n"%(list2Bulking[xBulk]-list1Bulking[xBulk])) #kcal #dois de quatro condições
        print("CONDIÇÃO OS DOIS VALORES SAO MENORES")
    elif list2Bulking[xBulk]<list1Bulking[xBulk] and list2Bulking[xBulk]>list1Bulking[xBulk] and xBulk==5:
        print("Está faltando %.2f de kcal, no bulking\n"%kcalBulkPROTLproth)
        print("CONDIÇÃO O PROTL É MAIOR E O PROTH É MENOR")
    elif list2Bulking[xBulk]>list1Bulking[xBulk] and list2Bulking[xBulk]<list1Bulking[xBulk] and xBulk==5:
        print("Está faltando %.2f de kcal, no bulking\n"%kcalBulkprotlPROTH)
        print("CONDIÇÃO O PROTL É MENOR E O PROTH É MAIOR")
    elif list2Bulking[xBulk]<list1Bulking[xBulk] and list2Bulking[xBulk]<list1Bulking[xBulk] and xBulk==5:
        print("Está faltando %.2f de kcal, no bulking\n"%kcalBulkPROTLPROTH)
        print("CONDIÇÃO OS DOIS VALORES SAO MAIORES")
    xBulk+=1
while xCut<6:
    if list2Cutting[xCut]>list1Cutting[xCut] and xCut==2:
        print("\nEstá faltando %.2f de carboidrato, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==3:
        print("Está faltando %.2f de proteína total, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==0:
        print("Está faltando %.2f de proteína de baixo valor biológico, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==1:
        print("Está faltando %.2f de proteína de alto valor biológico, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==4:
        print("Está faltando %.2f de gordura, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    elif list2Cutting[xCut]>list1Cutting[xCut] and xCut==5:
        print("Está faltando %.2f de kcal, no cutting"%(list2Cutting[xCut]-list1Cutting[xCut]))
    xCut+=1
#protl = 0
#proth = 0
#protlmeta = 1
#prothmeta = 1
#if protl<protlmeta and proth<prothmeta:
#    pass
#elif protl>protlmeta and proth<prothmeta:
#    pass
#elif protl<protlmeta and proth>prothmeta:
#    pass
#elif protl>protlmeta and proth>prothmeta:
#    pass