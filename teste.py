import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb['comida']
mycol2 = mydb['Layout']
x = mycol.find()
#list = ["carb","protl","proth","fat"]
#for a in range(len(list1)):
#    for k in range(len(list)):
#        if a==0:
#            carb += eval(list1[a].get(list[k]))
#        elif a==1:
#            protl += eval(list1[a].get(list[k]))
#        elif a==2:
#            proth += eval(list1[a].get(list[k]))
#        elif a==3:
#            fat += eval(list1[a].get(list[k]))
#print("{}\n{}\n{}\n{}".format(carb,protl,proth,fat))