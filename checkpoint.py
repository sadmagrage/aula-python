idade = list(input("Digite as idades separadas por um espaço assim '10 11 12 13 14'\n"))
ya = ""
listanova = []
x=0
while x<len(idade):
    if x == len(idade)-1:
        ya += idade[x]
        listanova.append(ya)
    elif idade[x] == " ":
        listanova.append(ya)
        ya = ""
    elif idade[x] != " ":
        ya += idade[x]
    x+=1