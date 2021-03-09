# Importação das bibliotecas
import requests  # A biblioteca resquests é a responsável pela requisão da API
import os


# Função para limpar o terminal
def limpar():
    if os.name == 'nt':  # Condicional para identificar o sistema operacional Windows
        os.system('cls')  # Comando para limpar o terminal
    else:
        os.system('clear')  # Comando para limpar o terminal caso o sistema operacional seja Linux


# Função para printar o cabeçalho
def cabecalho():
    print('='*25)
    print('    BUSCADOR DE CEP')
    print('='*25)


# Função com a requisição da API
def cep_consulta(cep):
    # Validação do formato do CEP
    if len(cep) != 8 and cep.isalnum() == True:
        print('CEP inválido.')
    else:
        # Requisição da API
        try:  # Try except para o caso de a api estar com problemas de funcionamento
            requisicao = requests.get('https://viacep.com.br/ws/' + cep + '/json/')
            json_cep = requisicao.json()
            return json_cep
        except Exception as err:
            print(f'Ocorreu um erro: {err}')


# Função para imprimir os detalhes do CEP informado
def detalhes(informacoes):
    print(f'CEP: {informacoes["cep"]}')
    print(f'Estado: {informacoes["uf"]}')
    print(f'Cidade: {informacoes["localidade"]}')
    print(f'Bairro: {informacoes["bairro"]}')
    print(f'Logradouro (rua, av., etc.): {informacoes["logradouro"]}')


while True:
    limpar()
    cabecalho()

    # Decisão para buscar o CEP ou fechar o programa
    opcao = str(input('Digite um número de CEP(apenas números) ou SAIR para fechar: ')).upper().strip()
    if opcao == 'SAIR':
        print('Saindo...')
        break
    else:
        try:  # Try except para o caso de o cep não existir
            info = cep_consulta(opcao)
            detalhes(info)
        except Exception:
            print('CEP não encontrado')

    # Decisão para continuar ou fechar o programa
    continuar = str(input('Deseja continuar a execução?[s/n] ')).upper()
    if continuar == 'S':
        limpar()
    else:
        print('Obrigado por utilizar o buscador de CEP!')
        break
