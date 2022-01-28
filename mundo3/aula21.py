# exercicio 101
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO!'


nasc = int(input('Em que voce nasceu? '))
print(voto(nasc))

#exercicio 102
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: mostra o processo.
    :return: retorna o resultado.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(9, show=True))

# exercicio 103
def ficha(jog='<Desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Quantos gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n .strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

# exercicio 104
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digte um numero inteiro valido!\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero {n}.')

# exercicio 105
def notas(*n, sit=False):
    """
    ->Funcao para analisar notas e situacoes de varios alunos
    :param n: uma ou mais notas dos alunos (aceita varias).
    :param sit: valor opcinal, indicando se deve ou nao adicionar situcao.
    :return: dicionario com varias informacoes sobre a situacao do turma.
    """"
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5, 5, 1, sit=True)
print(resp)

# exercicio 106
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'')
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)



comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Funcao ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!')
