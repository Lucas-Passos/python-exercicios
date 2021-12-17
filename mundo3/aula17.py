# exercicio 78
listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('==' * 20)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valorr digitado foi {maior} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()

# exercicio 79
numeros = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
        r = str(input('Deseja continuar [S/N]')).strip().upper()
    if r in 'N':
        break
numeros.sort()
print(f'Voce digitou os valores {numeros}')

# exercicio 80
valores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
            print(f'Adicionado na posicao {pos} da lista...')
            break
        pos += 1
print(f'Os valores digitados em ordem foram {valores}')

# exercicio 81
nums = []
while True:
    nums.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
print('==' * 20)
nums.sort(reverse=True)
print(f'voce digitou {len(nums)} numeros')
print(f'Os valores digitados foram: {nums}')
if 5 in nums:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 nao esta na lista')

# exercicio 82
val = list()
valp = list()
vali = list()
while True:
    val.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
for i, v in enumerate(val):
    if v % 2 == 0:
        valp.append(v)
    else:
        vali.append(v)
print('=' * 20)
print(f'A lista completa e: {val}')
print(f'A lista de valores pares e: {valp}')
print(f'A lista de valores impares e: {vali}')

# exercicio 83
expr = str(input('Digite a expressao: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print('Sua expressao esta correta')
else:
    print('Sua expressao esta errada')
