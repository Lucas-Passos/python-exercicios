import math
import random
from pygame import mixer


# exercicio 17
co = float(input("cateto oposto: "))
ca = float(input("cateto adjacente: "))
h = math.hypot(co, ca)
print("a hipotenusa vale: {:.2f}".format(h))

# exercicio 18
ang = float(input("digite um angulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
ta = math.tan(math.radians(ang))
print("o angulo {} tem seno de {:.2f} coseno de {:.2f} e tangente de {:.2f}".format(
    ang, sen, cos, ta))

# exercicio 19
n1 = str(input("aluno 1: "))
n2 = str(input("aluno 2: "))
n3 = str(input("aluno 3: "))
n4 = str(input("aluno 4: "))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print("o escohldo foi {}.".format(escolhido))

# exercicio 20
n1 = str(input("aluno 1: "))
n2 = str(input("aluno 2: "))
n3 = str(input("aluno 3: "))
n4 = str(input("aluno 4: "))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print("a ordem de apresentacao sera:")
print(alunos)

# exercicio 21
mixer.init()
mixer.music.load('good.mp3')
mixer.music.play()
input('playing')
