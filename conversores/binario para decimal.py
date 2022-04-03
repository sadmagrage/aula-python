num = input("digite o numero binário: ")
i=0
aa=0
bb=len(num)-1
while i<len(num):
    if num[i] == "0" or num[i] == "1":
        numa=int(num[i])*2**bb
        bb-=1
        aa+=numa
        i+=1
    else:
        print("o número digitado é inválido")
        break
else:
    print(aa)