# Um programa de interface gráfica que deve ser capaz de:
# -Armazenar o site/software p/ o qual a senha será gerado
# -Armazenar o usuário/e-mail
# -Possibilitar a configuração do tamanho da senha 
# - [BONUS]-Tocar música de fundo ao iniciar o programa

import random
import PySimpleGUI as sg

class PassGen:
    def __init__(self):
        sg .theme('Black')
        layout = [
            [ sg.Text('Site/Software', size=(10,1)),
             sg.Input(key='site', size=(20,1))],
             [sg.Text('E-mail/Usuário', size=(10,1)),
              sg.Input(key='usuário', size=(20,1))],
              
        ]
    def Iniciar(self):
        pass
    def salvar_senha(self):
        pass

    gen = PassGen()
    gen.Iniciar()