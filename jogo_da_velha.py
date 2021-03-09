# Importação das bibliotecas
import PySimpleGUI as sg  # PySimpleGUI é a biblioteca responsável pela representação gráfica do jogo
from random import randint

# Variáveis de controle
jogadas = 0  # Controle de jogadas
quem_joga = 2  # Controle de quem joga
max_jogadas = 9  # Variável para o máximo de jogadas possíveis


# Função para a atribuição da tela do jogo a uma variável
def jogo():
    # Dicionário para simplicar a criação do estilo dos botões
    botao = {'size': (7, 2), 'font': ('Franklin Gothic Book', 25), 'button_color': ('black', 'white')}
    # Layout utilizado para a criação da tela do jogo
    layout_jogo = [
        [sg.Button('', **botao, key=1), sg.Button('', **botao, key=2), sg.Button('', **botao, key=3)],
        [sg.Button('', **botao, key=4), sg.Button('', **botao, key=5), sg.Button('', **botao, key=6)],
        [sg.Button('', **botao, key=7), sg.Button('', **botao, key=8), sg.Button('', **botao, key=9)],
        [sg.Text('Bem vindo ao jogo da velha!\nO jogo começou', size=(50, 3), justification='center',
                 background_color='white', text_color='black', key='text')]]
    return sg.Window('Jogo da Velha', layout=layout_jogo, background_color='black', size=(425, 400), finalize=True)


# Função para a atribuição da tela de vitória a uma variável
def vitoria():
    # Layout utilizado para a criação da tela de vitória
    layout_vitoria = [
        [sg.Text('', font=('Franklin Gothic Book', 25), size=(50, 1), justification='center', key='vit',
                 background_color='black')],
        [sg.Button('Jogar novamente', size=(15, 3), key='jogar_novamente', button_color=('black', 'white'),
                   pad=(80, 3))],
        [sg.Button('Fechar o jogo', size=(15, 3), key='fechar_jogo', button_color=('black', 'white'), pad=(80, 0))]]
    return sg.Window('ACABOU', layout=layout_vitoria, background_color='black', size=(320, 200), finalize=True)


# Atribuição da tela às variáveis, as duas variáveis estão recebendo a mesma tela para evitar conflito na hora de rodar
# o programa
janela_jogo, janela_vitoria = jogo(), None  # None para evitar o erro de key ao utilizar duas telas


# Função para executar as jogadas do jogador
def jogador():
    global jogadas, quem_joga, max_jogadas  # Declaração das variáveis de escopo global

    # Condição para verificação se é possível realizar jogadas
    if quem_joga == 2 and jogadas < max_jogadas:
        for i in range(1, 10):  # For para cobrir todos os eventos possíveis de click, i representa o número das keys
            if event == i:
                # Condição para impedir de jogar em uma casa já ocupada
                if janela_jogo[i].GetText() == 'X' or janela_jogo[i].GetText() == 'O':
                    janela_jogo['text'].update(value='Casa já ocupada, jogue novamente')
                else:
                    janela_jogo[i].update('X')
                    break  # Break para evitar que o for continue executando desnecessáriamente quando o evento já
                           # houver ocorrido
        quem_joga = 1  # Mudança de jogador
        jogadas += 1  # Contador de jogadas


# Função para executar as jogadas da máquina
def computador():
    global jogadas, quem_joga, max_jogadas  # Declaração das variáveis de escopo global

    # Condição para verificação se é possível realizar jogadas
    if quem_joga == 1 and jogadas < max_jogadas:
        while True:  # While para executar a função até que seja realizada uma jogada válida
            chave_gerada = randint(1, 9)  # Randint para o sorteio de uma key aleatória
            # Condicional para que a máquina não jogue em uma casa já ocupada
            if janela_jogo[chave_gerada].GetText() == '':
                janela_jogo[chave_gerada].update('O')
                break  # Break para parar a execução do while assim que uma jogada válida é realizada
        quem_joga = 2  # Mudança de jogador
        jogadas += 1  # Contador de jogadas


# Função para verificar as condições de vitória
def verificar_vitoria():
    global janela_vitoria  # Declaração das variáveis de escopo global

    # Variáveis para alcançar as outras casas dentro do for
    b = 2
    c = 3
    for a in range(1, 8, 3):
        # Condicional para verificar a vitória no caso das linhas
        if (janela_jogo[a].GetText() == 'X' or janela_jogo[a].GetText() == 'O') and (janela_jogo[a].GetText() ==
                                                                                     janela_jogo[b].GetText() ==
                                                                                     janela_jogo[c].GetText()):
            janela_vitoria = vitoria()  # Atribuição da tela de vitória para que ela apareça
            # Atualização da tela para que apareça a mensagem de qual jogador ganhou
            janela_vitoria['vit'].update(value=f'O jogador {janela_jogo[a].GetText()} venceu!')
            return True  # Este e os demais retornos serão utilizados na condicional de verificação de vitória
        # Adição de valores às demais variáveis para alcançar os valores de cada linha
        b += 3
        c += 3

    # Variáveis para alcançar as outras casas dentro do for
    e = 4
    f = 7
    for d in range(1, 4, 1):
        # Condicional para verificar a vitória no caso das colunas
        if (janela_jogo[d].GetText() == 'X' or janela_jogo[d].GetText() == 'O') and (janela_jogo[d].GetText() ==
                                                                                     janela_jogo[e].GetText() ==
                                                                                     janela_jogo[f].GetText()):
            janela_vitoria = vitoria()  # Atribuição da tela de vitória para que ela apareça
            janela_vitoria['vit'].update(value=f'O jogador {janela_jogo[d].GetText()} venceu!')
            return True
        # Adição de valores às demais variáveis para alcançar os valores de cada coluna
        e += 1
        f += 1

    # Condicionais para verificar a vitória no caso das diagonais principal e secundária
    if (janela_jogo[1].GetText() == 'X' or janela_jogo[1].GetText() == 'O') and (janela_jogo[1].GetText() ==
                                                                                 janela_jogo[5].GetText() ==
                                                                                 janela_jogo[9].GetText()):
        janela_vitoria = vitoria()
        janela_vitoria['vit'].update(value=f'O jogador {janela_jogo[1].GetText()} venceu!')
        return True
    if (janela_jogo[3].GetText() == 'X' or janela_jogo[3].GetText() == 'O') and (janela_jogo[3].GetText() ==
                                                                                 janela_jogo[5].GetText() ==
                                                                                 janela_jogo[7].GetText()):
        janela_vitoria = vitoria()
        janela_vitoria['vit'].update(f'O jogador {janela_jogo[3].GetText()} venceu!')
        return True

    # Condicional para verificar se o jogo deu velha
    if jogadas == max_jogadas:
        janela_vitoria = vitoria()
        janela_vitoria['vit'].update(value='# DEU VELHA #')
        return True

    return False  # Este e os demais retornos serão utilizados na condicional de verificação de vitória


while True:
    window, event, values = sg.read_all_windows()  # Comando para ler as duas telas

    # Condicionais para parar a execução do programa ao fechar uma das duas telas
    if window == janela_vitoria and (event == sg.WIN_CLOSED or event == 'fechar_jogo'):
        break
    if window == janela_jogo and event == sg.WIN_CLOSED:
        break
    # Condicional para jogar novamente
    if window == janela_vitoria and event == 'jogar_novamente':
        for i in range(1, 10, 1):  # For para zerar as casas do jogo
            janela_jogo[i].update('')
        jogadas = 0  # Reset do número de jogadas
        quem_joga = 2  # Indicação do primeiro a jogar
        janela_vitoria.hide()  # Função para fechar a janela de vitória automaticamente

    # Chamada das funções para rodar o jogo
    jogador()
    if verificar_vitoria() == False:  # Condicional para caso o jogador ganhe a máquina não jogue bugando o jogo
        computador()
        verificar_vitoria()
