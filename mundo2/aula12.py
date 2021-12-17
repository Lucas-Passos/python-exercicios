from random import randint
from datetime import date
# exercicio 36
casa = float(input('Valor da casa: R$'))
sal = float(input('Qual o salario do comprador: R$'))
t = int(input('Quantos anos de financiamento? '))
p = casa / (t * 12)
min = sal / 100 * 30
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, t), end='')
print('a prestacao sera de R${:.2f}'.format(p))
if p <= min:
    print('Eprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')

# exercicio 37
num: int = int(input('Digite um numero inteiro: '))
print('[1] converter para BINARIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
op = int(input('Sua opcao:'))
if op == 1:
    print('O numero {} em binario e {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O numero {} em octal e {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O numero {} em hexadecimal e {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida!')

# exercicio 38
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print('O primeiro valor e maior')
elif n2 > n1:
    print('O segundo valor e maior')
else:
    print('Os valores sao iguais')

# exercicio 39
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 18:
    saldo = 18 - idade
    ali = atual + saldo
    print('Voce precisa se alistar em {} anos'.format(saldo))
    print('Seu alistamento sera em {}'.format(ali))
elif idade > 18:
    saldo = idade - 18
    ali = atual - saldo
    print('Voce deveria ter se alistado a {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ali))
else:
    print('Voce deve se alistar nesse ano')

# exercicio 40
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Media {:.1f}'.format(m))
if m < 5:
    print('REPROVADO!')
elif 7 > m >= 5:
    print('RECUPERACAO!')
else:
    print('APROVADO!')

# exercicio 41
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificacao: MIRIM')
elif 9 < idade <= 14:
    print('Classificacao: INFANTIL')
elif 14 < idade <= 19:
    print('Classificacao: JUNIOR')
elif 19 < idade <= 25:
    print('Classificao: SENIOR')
else:
    print('Classificacao: MASTER')

# exercicio 42
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('E possivel formar um triangulo', end=' ')
    if s1 != s2 != s3 != s1:
        print('ESCALENO')
    elif s1 == s2 == s3:
        print('EQUILATERO')
    else:
        print('ISOSCELES')
else:
    print('Nao e possivel formar um triangulo.')

# exercicio 43
peso = float(input('Qual seu peso? (Kg) '))
alt = float(input('Qual sua altura? (m) '))
imc = peso / (alt ** 2)
print('O IMC dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')

# exercicio 44
valor = float(input('Preco das compras R$'))
print(''''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque.
[2] a vista no cartao.
[3] 2x no cartao.
[4] 3x ou mais no cartao.''')
pag = int(input('Escolha a opcao de pagamento:'))
if pag == 1:
    des = (valor / 100) * 10
    valor = valor - des
    print('O valor a pagar sera de R${:.2f}'.format(valor))
elif pag == 2:
    des = (valor / 100) * 5
    valor = valor - des
    print('O valor a pagar sera de R${:.2f}'.format(valor))
elif pag == 3:
    parcela = valor / 2
    print(
        'Sua compra sera parcelada em 2x de R${:.2f}  SEM JUROS'.format(parcela))
    print('O valor a pagar sera de R${:.2f}'.format(valor))
elif pag == 4:
    juros = (valor / 100) * 20
    valor = valor + juros
    parcelas = int(input('Qual o numero de parcelas: '))
    parcela = valor / parcelas
    print('O valor a pagar sera de R${:.2f}'.format(valor))
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(
        parcelas, parcela))
else:
    print('Opcao invalida!')

print('''JAN-KEN-PO
[0] Pedra
[1] Papel
[2] Tesoura''')
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
jan = int(input('Escolha uma opcao:'))
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jan]))

if comp == 0:
    if jan == 0:
        print('EMPATE!')
    elif jan == 1:
        print('JOGADOR VENCE!')
    elif jan == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')
elif comp == 1:
    if jan == 0:
        print('COMPUTADOR VENCE!')
    elif jan == 1:
        print('EMPATE!')
    elif jan == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')
elif comp == 2:
    if jan == 0:
        print('JOGADOR VENCE!')
    elif jan == 1:
        print('COMPUTADOR VENCE!')
    elif jan == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
