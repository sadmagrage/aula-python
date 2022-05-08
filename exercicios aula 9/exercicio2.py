idade = list(input("Digite as idades separadas por um espaço assim '10 11 12 13 14'\n"))
ya = ""
newIdade = []
x=0
while x<len(idade):
    if x == len(idade)-1:
        ya += idade[x]
        newIdade.append(ya)
    elif idade[x] == " ":
        newIdade.append(ya)
        ya = ""
    elif idade[x] != " ":
        ya += idade[x]
    x+=1
podeVotar = []
naoPodeVotar = []
newIdade = list(map(int,newIdade))
for x in range(len(newIdade)):
    if newIdade[x]>=16:
        podeVotar.append(newIdade[x])
    elif newIdade[x]<0:
        pass
    elif newIdade[x]<16:
        naoPodeVotar.append(newIdade[x])
mediaNaoPodeVotar = 0
for x in range(len(naoPodeVotar)):
    mediaNaoPodeVotar += naoPodeVotar[x]
if len(naoPodeVotar)>=1:
    mediaNaoPodeVotar/=len(naoPodeVotar)
print("{} alunos podem votar.".format(len(podeVotar)))
print("{} anos é a média da idade de alunos que não podem votar.".format(mediaNaoPodeVotar))