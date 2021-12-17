from random import randint
# exercicio 72
cont = ('zeor', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Dgite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Voce digitou o numero  {cont[num]}')

# exercicio 73
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atletico',
         'Botafogo', 'Atletico-PR', 'Bahia', 'Sao Paulo', 'Fluminense',
         'Sport Recife', 'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta ',
         'Atletico-GO')
print('-=' * 20)
print(f'Lista de times do brasileirao: {times}')
print('-=' * 20)
print(f'Os 5 primeiros sao {times[0:5]}')
print('-=' * 20)
print(f'Os 4 ultimos sao {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 20)
print(f'O Chapecoense esta na {times.index("Chapecoense")+1} posicao')
print('-=' * 20)

# exercicio 74
numeros = (randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10),
           randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

# exercicio 75
num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posicao')
else:
    print(f'O valor 3 nao foi digitado.')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')

# exercicio 76
print('-' * 30)
print('{:^30}'.format('LISTAGEM DE PRECOS'))
print('-' * 30)
listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 9.90,
            'Estojo', 4.50,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 69.90,
            'Canetas', 12.90,
            'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')

# exercicio 77
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
