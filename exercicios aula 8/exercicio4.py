listnum = list(input("Digite valores reais separadas por um espaço assim '10 11 12 13 14'\n"))
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
countp = 0
countn = 0
listanova = list(map(float,listanova))
for x in listanova:
    if x>0:
        countp+=1
    elif x<0:
        countn+=1
listanova.sort()
print("{} números positivos foram inseridos.\n{} números negativos foram inseridos.\nO menor valor inserido foi : {}".format(countp,countn,listanova[0]))