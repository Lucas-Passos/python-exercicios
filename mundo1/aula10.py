from datetime import date
# exercicio 28
from random import randint
from time import sleep
comp = randint(0, 5)
print('Acerte o numero em que vou pensar!')
print('ESTOU PENSANDO...')
sleep(2)
jogador = int(input('Em que numero eu pensei? '))
if jogador == comp:
    print('Voce acertou!')
else:
    print("Voce errou eu pensei no numero {}".format(comp))

# exercicio 29
vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    m = (vel - 80) * 7
    print(
        'voce excedeu o limite 80km/h e foi multado no valor de R${:.2f}'.format(m))
print('tenha um bom dia! dirija com cuidado!')

# exercicio 30
num = int(input('Digite um nummero qualquer: '))
resultado = num % 2
if resultado == 1:
    print('O numero {} e IMPAR'.format(num))
else:
    print('O numero {} e PAR'.format(num))

# exercicio 31
dis = float(input('Digite a distancia da viagem:'))
if dis <= 200:
    dis = dis * 0.5
    print('A passagem vai custar {}'.format(dis))
else:
    dis = dis * 0.45
    print('A passagem vai custar {}'.format(dis))

# exercicio 32
ano = int(input('Que ano voce quer analisar?Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} e bissexto'.format(ano))
else:
    print('O ano {} nao e bissexto'.format(ano))

# exercicio 33
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
n3 = int(input('Terceiro valor:'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n1 > n2 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))

# exercicio 34
sal = float(input('Qual o salario do funcionario? R$:'))
if sal >= 1250:
    aum = (sal / 100 * 10) + sal
else:
    aum = (sal / 100 * 15) + sal
print('Quem ganhva R${:.2f} passa a ganhar R${:.2f}'.format(sal, aum))


# exercicio 35
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('E possivel formar um triangulo')
else:
    print(" Nao e possivel formar um triangulo")
