# Importação das bibliotecas, majoritariamente os comando são da biblioteca pandas, biblioteca usada para Data Science
# que possui comandos de manipulação de arquivos excel, para informações mais detalhadas use a documentação oficial
# => https://pandas.pydata.org/pandas-docs/stable/
import pandas as pd
import os


# Função para limpar o terminal,
def limpar():
    if os.name == 'nt':  # Condicional para identificar o sistema operacional Windows
        os.system('cls')  # Comando para limpar o terminal
    else:
        os.system('clear')  # Comando para limpar o terminal caso o sistema operacional seja Linux


# Função para limpar o terminal e printar o arquivo
def limpar_printar(excel):
    limpar()
    print(excel)


# Função para printar o cabeçalho
def cabeca():
    limpar()
    print('#'*25)
    print('     Editor de Excel')
    print('#' * 25)


# Função para abrir o arquivo desejado
def abrir_arquivo():
    while True:
        try:  # Try except para caso ocorra erros na abertura do arquivo
            caminho = str(input('Digite o caminho do arquivo que deseja abrir:'
                                ' [Entrada e saida de arquivos xls estão desabilitadas]'
                                '\nex.: C:/caminho/arquivo/nome_arquivo.extensão'
                                '\n=> '))
            if caminho[len(caminho) - 3::1] == 'csv':  # Condicional para detectar automáticamente arquivos .csv
                arquivo = pd.read_csv(caminho, delimiter=';')  # Transformação do arquivo aberto em pandas Data Frame
            else:
                arquivo = pd.read_excel(caminho)  # Transformação do arquivo aberto em pandas Data Frame

            print(arquivo)
            checagem = int(input('^Este arquivo foi encontrado^'  # Menu para a tomada de decisão do usuário
                                 '\n[1] Continuar com este arquivo'
                                 '\n[2] Abrir outro arquivo'
                                 '\n[3] Fechar programa'
                                 '\n=> '))
            # Estrutura condicional para redirecionamento da decisão
            if checagem == 1:
                alteracoes(arquivo)
            elif checagem == 2:
                limpar()
                abrir_arquivo()  # Recursividade da função para caso o usuário deseje abrir outro arquivo
            elif checagem == 3:
                return print('Obrigado por utilizar o editor de excel!')  # Retorno para o caso de fechamento do programa
            break
        except Exception:  # Except para caso o arquivo não seja encontrado
            print('Arquivo não encontrado.')


# Função do menu de alterações
def alteracoes(excel):
    limpar_printar(excel)

    alterar = int((input('O que deseja alterar:'
                         '\n[1] Colunas'
                         '\n[2] Linhas'
                         '\n[3] Índices'
                         '\n[4] Valores'
                         '\n[5] Salvar arquivo'
                         '\n[6] Abrir outro arquivo'
                         '\n[7] Fechar programa'
                         '\n=> ')))
    # Estrutura condicional para redirecionamento da decisão, para cada decisão existe uma função respectiva
    if alterar == 1:
        coluna(excel)

    elif alterar == 2:
        linha(excel)

    elif alterar == 3:
        indice(excel)

    elif alterar == 4:
        valor(excel)

    elif alterar == 5:
        salvar_arquivo(excel)

    elif alterar == 6:
        abrir_arquivo()

    elif alterar == 7:
        return print('Obrigado por utilizar o editor de excel!')  # Retorno para o caso de fechamento do programa


# Função para a decisão de alteração das colunas
def coluna(excel):
    limpar_printar(excel)

    colunas = int(input('Alterar colunas'
                        '\n[1] Adicionar colunas'
                        '\n[2] Remover colunas'
                        '\n[3] Renomear colunas'
                        '\n[4] Reorganizar colunas'
                        '\n[5] Voltar ao menu'
                        '\n=> '))
    # Estrutura condicional para redirecionamento da decisão
    if colunas == 1:
        limpar_printar(excel)  # Em todos os casos existe a chamada da função para limpar o terminal e printar novamente
                               # a tabela
        nome_coluna = input('Digite o nome que deseja para a nova coluna:'    
                            '\n=> ')
        excel.insert(loc=len(excel.columns.values), column=nome_coluna, value=0)
        alteracoes(excel)  # Em todos os casos ao final da alteração o menu de alterações é chamado novamente

    elif colunas == 2:
        limpar_printar(excel)
        nome_coluna = input('Digite o(s) nome(s) da(s) coluna(s) que deseja excluir:'
                            '\nPara mais de uma coluna separe os nomes apenas por "/"'
                            '\nAperte "n" para voltar'
                            '\n=> ')
        nomes = nome_coluna.split('/')
        excel = excel.drop(nomes, axis=1)
        alteracoes(excel)

    elif colunas == 3:
        limpar_printar(excel)
        numero_coluna = int(input('Digite o número da coluna que deseja renomear'
                                  ' [A numeração começa a partir do 0, 1° coluna = 0, 2° coluna = 1, etc.]'
                                  '\n=> '))
        nome_coluna = input('Digite o novo nome da coluna'
                            '\n=> ')
        excel.columns.values[numero_coluna] = nome_coluna
        alteracoes(excel)

    elif colunas == 4:
        limpar_printar(excel)
        nome_coluna = input('Digite o nome das colunas na ordem que deseja organizar'
                            '\nSepare os nomes apenas por "/"'
                            '\n=> ')
        nomes = nome_coluna.split('/')
        excel = excel[nomes]
        alteracoes(excel)

    elif colunas == 5:
        alteracoes(excel)


# Função para a alteração das linhas
def linha(excel):
    limpar_printar(excel)

    linhas = int(input('Alterar linhas'
                       '\n[1] Adicionar linhas'
                       '\n[2] Remover linhas'
                       '\n[3] Voltar ao menu'
                       '\n=> '))

    if linhas == 1:
        limpar_printar(excel)
        excel.loc[len(excel)] = 0
        alteracoes(excel)

    elif linhas == 2:
        limpar_printar(excel)
        numero_linha = int(input('Digite o número da linha que deseja excluir'
                                 ' [Use o índice das linhas apresentado à esquerda das linhas]'
                                 '\n=> '))
        excel = excel.drop([numero_linha - 1])
        alteracoes(excel)

    elif linhas == 3:
        alteracoes(excel)


# Função para a alteração dos índices
def indice(excel):
    limpar_printar(excel)

    indices = int(input('Alterar índices'
                        '\n[1] Remover índice'
                        '\n[2] Adicionar índice'
                        '\n[3] Voltar ao menu'
                        '\n=> '))

    if indices == 1:
        limpar_printar(excel)
        nome_indice = input('Digite o nome do índice a ser removido:'
                            '\n=> ')
        excel = excel.reset_index(level=nome_indice)
        alteracoes(excel)

    elif indices == 2:
        limpar_printar(excel)
        nome_indice = input('Digite o nome do índice a ser adicionado:'
                            '\n=> ')
        excel = excel.set_index(nome_indice)
        alteracoes(excel)

    elif indices == 3:
        alteracoes(excel)


# Função para a alteração das células
def valor(excel):
    limpar_printar(excel)
    linha_valor = int(input('Digite o número da linha [Use o índice das linhas apresentado à esquerda das linhas]'
                            '\n=> '))
    coluna_valor = int(input('Digite o número da coluna'
                             ' [A numeração começa a partir do 0, 1° coluna = 0, 2° coluna = 1, etc.]'
                             '\n=> '))
    valor_alteracao = input('Digite o que deseja adcionar à celula'
                            '\n=> ')
    excel.values[linha_valor][coluna_valor] = valor_alteracao
    alteracoes(excel)


# Função para salvar o arquivo editado
def salvar_arquivo(excel):
    limpar_printar(excel)

    saida = input('Insira o local onde deseja salvar o arquivo:'
                  '\nex.: C:/caminho/arquivo/saida/'
                  '\n=> ')
    formato = input('Insira o nome com o formato de saida do arquivo:'
                    '\nex.: tabela1.csv'
                    '\n=> ')
    if formato[len(formato) - 3::1] == 'csv':
        excel.to_csv(saida + formato, sep=';', index=True)
    else:
        excel.to_excel(saida + formato)
    alteracoes(excel)


# A não utilização de um while é devido ao fato de que as funções estão entrelaçadas entre si de modo que não há
# necessidade para uma estrutura de repetição, o que facilita até mesmo o fechamento do programa, os returns são os
# pontos de parada do programa
cabeca()
abrir_arquivo()
