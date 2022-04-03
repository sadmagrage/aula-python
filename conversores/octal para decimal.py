num = input("digite o numero octal: ")
i=0
aa=0
bb=len(num)-1
while i<len(num):
    numa=int(num[i])*8**bb
    bb-=1
    aa+=numa
    i+=1
else:
    print(aa)