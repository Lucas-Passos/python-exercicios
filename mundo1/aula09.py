# exercicio 22
nome = str(input('digite seu nome completo:')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
separa = nome.split()
print(separa[0], len(separa[0]))

# exercicio 23
num = int(input(' digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))

# exercicio 24
cid = str(input('em que cidade voce nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')

# exercicio 25
nome = str(input('qual seu nome completo? ')).strip()
print('seu nome tem Silva? {}'.format('silva' in nome.lower()))

# exercicio 26
frase = str(input('digite uma frase: ')).strip()
a = frase.lower()
print('a letra A aparece {} vezes na frase.'.format(a.count('a')))
print('a primeira letra A aparecceu na posicao {}.'.format(a.find('a')+1))
print('a ultima letra A apareceu na posicao {}.'.format(a.rfind('a')+1))

# exercicio 27
nome = str(input(' digite seu nome completo: ')).strip()
n = nome.split()
print('seu primeiro nome e: {}'.format(n[0]))
print('seu ultimo nome e: {}'.format(n[len(n)-1]))
