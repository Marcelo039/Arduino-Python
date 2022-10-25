
import PySimpleGUI as sg # Para interface gráfica
import pyfirmata # Para usar o Arduino

# Configurando variavel do arduino
Uno = pyfirmata.Arduino("COM3")
Uno.digital[2].mode = pyfirmata.OUTPUT

# Configurar e carregar interface gráfica
sg.theme('LightGrey6') 
layout = [ 
[ sg.Text('Controle do LED') ],
[ sg.Button('Ligar azul', key='ligA'),
sg.Button('Desligar azul', key='deslA') ] ,
[ sg.Button('Ligar vermelho', key='ligV'),
sg.Button('Desligar vermelho', key='deslV') ] 
]

janela = sg.Window('Python + Arduino', layout, size=(300, 200))

# Eventos
while True:
    evento, dado = janela.read()
    if evento == 'ligA':
        print("Ligando o LED")
        Uno.digital[2].write(1)
    elif evento == 'deslA':
        print("Desligando o LED")
        Uno.digital[2].write(0)
    elif evento == 'ligV':
        print("Ligando o LED")
        Uno.digital[3].write(1)
    elif evento == 'deslV':
        print("Desligando o LED")
        Uno.digital[3].write(0)
    elif evento == sg.WIN_CLOSED:
        break

janela.close()

