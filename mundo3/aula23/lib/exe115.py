from aula23.lib.interface import *
from aula23.lib.arquivo import *
from time import sleep

arq = 'cev.txt'

if not arqExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Listar o conteudo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa.
        header('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Sair do sistema.
        print('Saindo do sistema... Ate logo!')
        break
    else:
        # Digitou uma opcao errada no menu.
        print('\033[31mERRO! Digite uma opcao valida!\033[m')
    sleep(1)


