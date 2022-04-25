###  se o prot for maior que o meta, o prot recebe o valor do meta
metakcal = 5000 #gastobulk
prot = 100 #prot
metaprot = 100 #metaprot
if prot>= metaprot:
    prot=metaprot
kcal = prot*4+5600 #kcal = prot*4+carb*9+fat*9
resKcal = metakcal-kcal #criar variavel
if metakcal>kcal:
    print("Faltam kcals:",resKcal)
elif metakcal<=kcal:
    print("Passaram kcals:",-resKcal)