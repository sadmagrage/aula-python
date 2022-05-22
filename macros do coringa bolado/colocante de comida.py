import PySimpleGUI as sg
import pymongo

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb['comida']

mycol = pymongo.MongoClient("mongodb://localhost:27017/")["mydatabase"]['comida']

def form():
    try:
        x = mycol.find()
        id = str(len(list(x))+1)
        name = values['name']
        carb = values['carb']
        protl = values['protl']
        proth = values['proth']
        fat = values['fat']
        key = values['key']
        mydict = {"_id":id,"name":name,"carb":carb,"protl":protl,"proth":proth,"fat":fat,"key":key}
        x = mycol.insert_one(mydict)
    except:
        print("Não deu certo.")
    else:
        print("Importado com sucesso.")

def criar_janela_inicial():
    sg.theme('Black')
    layout = [
        [sg.Text("Nome"),sg.Input(key = "name",size = (20,1)),sg.Text("Carb"),sg.Input(key = "carb", size = (6,1))],
        [sg.Text("Protl"),sg.Input(key = "protl", size = (6,1)),sg.Text("Proth"),sg.Input(key = "proth", size = (6,1))],
        [sg.Text("Fat"),sg.Input(key = "fat", size = (6,1)),sg.Text("Key"),sg.Input(key = "key", size = (20,1))],
        [sg.Button("Importar para o banco de dados"), sg.Output(size = (22,5))]
    ]
    return sg.Window('Importar para o banco de dados', layout = layout, finalize = True)
janela = criar_janela_inicial()
while True:
    event, values = janela.read()
    if event == "Importar para o banco de dados":
        form()
    elif event == sg.WIN_CLOSED:
        break