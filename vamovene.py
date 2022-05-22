#lista = 
#lista1 = [[]]
#for y in range(len(lista)):
#    if len(lista1[-1])==3:
#        lista1.append([])
#        lista1[-1].append(lista[y])
#    else:
#        lista1[-1].append(lista[y])
#print(lista1)
#list1 = ["aa","bb","cc","dd","ee","ff","gg","hh","ii"]
#newLayout = [[],
#    ["ii"],
#    ["jj"]
#    ]
#for y in range(len(list1)):
#    if len(newLayout[-3])==6:
#        newLayout.insert(-2,[])
#        newLayout[-3].append(list1[y])
#    else:
#        newLayout[-3].append(list1[y])
#print(newLayout)
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb['comida']
x = mycol.find()
list1 = list(x)
print(list1[0].get("name"))