import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome'),sg.Input(key='nome')],
            [sg.Text('Idade'),sg.Input(key='idade')],
            [sg.Button('botao')]
        ]
        self.janela = sg.Window("Dados do Usuário").layout(layout)
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            print(f'nome: {nome}')
            mtp2 = int(idade)*2
            print(f'idade: {mtp2}')
tela=TelaPython()
tela.Iniciar()