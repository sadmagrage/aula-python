i = 0
list1 = [1,2,3,4,5,6]
list2 = [2,3,4,5,6,7]
while i<6:
    if list2[i]>list1[i] and i==0:
        print("Está faltando %.2f de carboidrato"%(list2[i]-list1[i]))
    elif list2[i]>list1[i] and i==1:
        print("Está faltando %.2f de proteína total"%(list2[i]-list1[i]))
    elif list2[i]>list1[i] and i==2:
        print("Está faltando %.2f de proteína de baixo valor biológico"%(list2[i]-list1[i]))
    elif list2[i]>list1[i] and i==3:
        print("Está faltando %.2f de proteína de alto valor biológico"%(list2[i]-list1[i]))
    elif list2[i]>list1[i] and i==4:
        print("Está faltando %.2f de gordura"%(list2[i]-list1[i]))
    elif list2[i]>list1[i] and i==5:
        print("Está faltando %.2f de kcal"%(list2[i]-list1[i]))
    i+=1