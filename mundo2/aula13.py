from datetime import datetime
from time import sleep

# exercicio 46
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('FOGOS!!!')

# exercicio 47
for par in range(2, 51, 2):
    if par % 2 == 0:
        print(par, end=' ')

# exercicio 48
soma = 0
cont = 0
for n in range(1, 501):
    if n % 3 == 0:
        soma += n
        cont += 1
print('A soma de todos os {} valores solicitados e {}'.format(cont, soma))

# exercicio 49
t = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 10):
    print('{} x {:2} = {}'.format(t, c, t*c))

# exercicio 50
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} numero: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('Voce informou {} numeros PARES e a soma foi {}'.format(cont, soma))

# exercicio 51
term = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = term + (10 - 1) * razao
for c in range(term, decimo + razao, razao):
    print('{} '.format(c), end='> ')
print('ACABOU!')

# exercicio 52
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[35m', end='')
        tot += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÂO É PRIMO!')

# exercicio 53
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase nao e um palindromo!')

# exercicio 54
maior = 0
menor = 0
atual = datetime.today().year
for pess in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E tambem tivemos {} pessoas menores de idade'.format(menor))

# exercicio 55
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

# exercicio 56

mediaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('-----{}ª PESSOA-----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1


mediaidade = somaidade / 4
print('A media de idade do grupo e de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(
    maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher))
