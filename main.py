import PySimpleGUI as sg

class Calculadora:

    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.resultado = 0
        self.operacao = ''
        self.eh_porcentagem = False

    def soma(self):
        self.resultado = self.numero1 + self.numero2

    def subtracao(self):
        self.resultado = self.numero1 - self.numero2
    
    def multiplicacao(self):
        self.resultado = self.numero1 * self.numero2
    
    def divisao(self):
        self.resultado = self.numero1 / self.numero2
    
calculadora = Calculadora()

############################################################################################

sg.theme('DarkAmber')

layout = [
    [sg.Text('0.0000', size=(27,1), justification='right', key='display')],
    [sg.Button('*', size=(2,1)), sg.Button('/', size=(2,1)), sg.Button('%', size=(2,1)), sg.Button('c', size=(2,1))],
    [sg.Button('7', size=(2,1)), sg.Button('8', size=(2,1)), sg.Button('9', size=(2,1)), sg.Button('√', size=(2,1))],
    [sg.Button('4', size=(2,1)), sg.Button('5', size=(2,1)), sg.Button('6', size=(2,1)), sg.Button('+', size=(2,1))],
    [sg.Button('1', size=(2,1)), sg.Button('2', size=(2,1)), sg.Button('3', size=(2,1)), sg.Button('-', size=(2,1))],
    [sg.Button('0', size=(9,1)), sg.Button(',', size=(2,1)), sg.Button('=', size=(2,1))]
]

window = sg.Window('Calculadora', layout)

def update_display(display_value: str):
    try:
        window['display'].update(value='{:,.4f}'.format(display_value))
    except:
        window['display'].update(value=display_value)
    
def refresh():
    calculadora.numero1 = 0
    calculadora.numero2 = 0
    calculadora.resultado = 0

def valida_caractere(event):
    try:
        int(event)
        return True
    except:
        return False

def realizaOperacao():

    if(calculadora.operacao == '+'):
        calculadora.soma()

    if(calculadora.operacao == '-'):
        calculadora.subtracao()

    if(calculadora.operacao == '*'):
        calculadora.multiplicacao()

    if(calculadora.operacao == '/'):
        calculadora.divisao()

    if(calculadora.operacao == '√'):
        calculadora.raiz_quadrada()
    
while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if valida_caractere(event):
        if(calculadora.numero1 != 0):
            calculadora.numero2 = float(event)
            update_display(event)
        else:
            calculadora.numero1 = float(event)
            update_display(event)
    elif event == 'c':
        refresh()
        update_display(0)
    elif event != '=':
        calculadora.operacao = event

    if event == '=':
        if(event == '%'):
            calculadora.numero2 = numero2 / 100
        realizaOperacao()
        print('resultado: ', calculadora.resultado)
        update_display(calculadora.resultado)
        refresh()

window.close()