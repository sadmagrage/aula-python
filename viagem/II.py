
metakcal = 5000 #gastobulk
prot = 95 #prot
kcal = prot*4+4600 #kcal = carb*4+fat*9 + prot*4
metaprot = 100 #metaprot
protResto = prot-metaprot
aa = kcal-(protResto)*4
aainverso = kcal-(-protResto)*4
printar = metakcal-aa
printarinverso = metakcal-aainverso

if protResto>0 and metakcal>kcal:
    print("Faltam kcals:",printar)
elif protResto<0 and metakcal<=kcal:
    print("Passaram kcals:",-printarinverso)
elif protResto<0 and metakcal>kcal:
    print("Faltam kcals:",-printarinverso)
elif protResto>0 and metakcal<=kcal:
    print("Passaram kcals:",-printar)
