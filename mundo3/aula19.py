from random import randint
from operator import itemgetter
from datetime import datetime
# exercicio 90
aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media do aluno: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
print('-' * 20)
for k, v in aluno.items():
    print(f' - {k} e igual a {v}')

# exercicio 91
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('==' * 15)
print('     == Ranking ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]}')

# exercicio 92
dados = {}
dados['nome'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho(0 nao tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + \
        ((dados['contratacao'] + 35) - datetime.now().year)
print('==' * 15)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')

# exercicio 93
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('==' * 15)
print(jogador)
print('==' * 15)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('==' * 15)
print(f'O jogador {jogador["nome"]} jogou  {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

# exercicio 94
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in ' SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('==' * 15)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A media de idade e de {media:4.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}, ', end='')
print()
print('Lista das pessoas que estao acima da media:', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
            print()
print('<<ENCERRADO>>')

# exercicio 95
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('==' * 15)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i+1:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('==' * 15)
while True:
    busca = int(input('Mostrar dados de qual jogador? (-1 para parar) '))
    if busca == -1:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
            print('=' * 15)
print('<<ENCERRADO>>')
