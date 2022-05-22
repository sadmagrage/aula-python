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



mydict = [
    {'_id': '01', 'name': 'leite', 'carb': '0.0452', 'protl': '0', 'proth': '0.0322', 'fat': '0.0325', "key": "LeiteGKey"},
    {'_id': '02', 'name': 'aveia', 'carb': '17/30', 'protl': '4.8/30', 'proth': '0', 'fat': '1.8/30', "key": "AveiaGKey"},
    {'_id': '03', 'name': 'udon', 'carb': '5.9/8.0', 'protl': '8.3/80', 'proth': '0', 'fat': '0.8/80', "key": "UdonGKey"},
    {'_id': '04', 'name': 'ovo', 'carb': '0.56/50', 'protl': '0', 'proth': '6.26/50', 'fat': '5.28/50', "key": "OvoGKey"},
    {'_id': '05', 'name': 'banana', 'carb': '22.84/100', 'protl': '1.09/100', 'proth': '0', 'fat': '0.33/100', "key": "BananaGKey"},
    {'_id': '06', 'name': 'frango', 'carb': '0', 'protl': '0', 'proth': '31.02/100', 'fat': '3.57/100', "key": "FrangoGKey"},
    {'_id': '07', 'name': 'arroz', 'carb': '28.59/100', 'protl': '2.38/100', 'proth': '0', 'fat': '0.21/100', "key": "ArrozGKey"},
    {'_id': '08', 'name': 'feijao', 'carb': '13.61/100', 'protl': '5.04/100', 'proth': '0', 'fat': '0.85/100', "key": "FeijaoGKey"},
    {'_id': '09', 'name': 'bife', 'carb': '0', 'protl': '0', 'proth': '27.29/100', 'fat': '15.01/100', "key": "BifeGKey"},
    {'_id': '10', 'name': 'couve', 'carb': '10.01/100', 'protl': '3.3/100', 'proth': '0', 'fat': '0.7/100', "key": "CouveGKey"},
    {'_id': '11', 'name': 'tempura', 'carb': '13.78/100', 'protl': '4.23/100', 'proth': '0', 'fat': '10.09/100', "key": "TempuraGKey"},
    {'_id': '12', 'name': 'pastel', 'carb': '0.438', 'protl': '10.1/100', 'proth': '0', 'fat': '18.3/100', "key": "PastelGKey"},
    {'_id': '13', 'name': 'ovofrito', 'carb': '0.43/46', 'protl': '0', 'proth': '6.24/46', 'fat': '6.76/46', "key": "OvoFritoGKey"},
    {'_id': '14', 'name': 'vo2', 'carb': '13', 'protl': '0', 'proth': '9', 'fat': '3.4', "key": "Vo2GKey"},
    {'_id': '15', 'name': 'udonamarelo', 'carb': '5.9/8.0', 'protl': '8.4/80', 'proth': '0', 'fat': '0.8/80', "key": "UdonAmareloGKey"},
    {'_id': '16', 'name': 'nescau', 'carb': '1.7/2.0', 'protl': '0.7/20', 'proth': '0', 'fat': '0', "key": "NescauGKey"},
    {'_id': '17', 'name': 'donabenta', 'carb': '5.4/8.0', 'protl': '6.6/80', 'proth': '0', 'fat': '1.1/80', "key": "DonaBentaGKey"},
    {'_id': '18', 'name': 'mussarela', 'carb': '0', 'protl': '0', 'proth': '38.0/100', 'fat': '17.0/100', "key": "MussarelaGKey"},
    {'_id': '19', 'name': 'molho', 'carb': '5.62/100', 'protl': '1.14/100', 'proth': '0', 'fat': '2.47/100', "key": "MolhoGKey"},
    {'_id': '20', 'name': 'pao', 'carb': '58.6/100', 'protl': '8.0/100', 'proth': '0', 'fat': '3.10/100', "key": "PaoGKey"},
    {'_id': '21', 'name': 'presunto', 'carb': '0', 'protl': '13.25/100', 'proth': '0', 'fat': '6.75/100', "key": "PresuntoGKey"},
    {'_id': '22', 'name': 'nesfitcacau', 'carb': '20.0/30', 'protl': '2.3/30', 'proth': '0', 'fat': '4.9/30', "key": "NesfitCacauGKey"},
    {'_id': '23', 'name': 'wgrowth', 'carb': '4.0/30', 'protl': '0', 'proth': '23.0/30', 'fat': '1.6/30', "key": "WheyGrowthGKey"},
    {'_id': '24', 'name': 'miojo', 'carb': '49.0', 'protl': '8.5', 'proth': '0', 'fat': '16.0', "key": "MiojoGKey"},
    {'_id': '25', 'name': 'whopper', 'carb': '54.0', 'protl': '18.5', 'proth': '18.5', 'fat': '35.0', "key": "WhopperGKey"},
    {'_id': '26', 'name': 'batata', 'carb': '20.01/100', 'protl': '1.71/100', 'proth': '0', 'fat': '0.1/100', "key": "BatataGKey"},
    {'_id': '27', 'name': 'lasanhaswift', 'carb': '55.0/300', 'protl': '19.0/300', 'proth': '0', 'fat': '11.0/300', "key": "LasanhaSwiftGKey"},
    {'_id': '28', 'name': 'sucodelaranja', 'carb': '20.0/200', 'protl': '1.4/200', 'proth': '0', 'fat': '0', "key": "SucoDeLaranjaGKey"},
    {'_id': '29', 'name': 'poctpoct', 'carb': '34.0', 'protl': '20.0', 'proth': '0', 'fat': '12.0', "key": "PoctPoctGKey"},
    {'_id': '30', 'name': 'supinochoc', 'carb': '12.0', 'protl': '0', 'proth': '10.0', 'fat': '2.7', "key": "SupinoChocGKey"},
    {'_id': '31', 'name': 'cup', 'carb': '43.0', 'protl': '7.5', 'proth': '0', 'fat': '12.0', "key": "CupGKey"},
    {'_id': '32', 'name': 'bigcrack', 'carb': '41.0', 'protl': '26.0', 'proth': '0', 'fat': '26.0', "key": "BigCrackGKey"},
    {'_id': '33', 'name': 'crisp', 'carb': '18.0', 'protl': '0', 'proth': '13.0', 'fat': '7.3', "key": "CrispGKey"},
    {'_id': '34', 'name': 'testeprot', 'carb': '0', 'protl': '23.19', 'proth': '208.74', 'fat': '0', "key": "TesteProtGKey"},
    {'_id': '35', 'name': 'testecarb', 'carb': '30/30', 'protl': '0', 'proth': '0', 'fat': '0', "key": "TesteCarbGKey"}
]
x = mycol.insert_many(mydict)