# #03 Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random   
# from random import randint

cont = 0
jogos = []
palpites = []

quantidade = int(input('Informe quantos jogos deseja gerar: '))

for i in range(quantidade):
    while cont < 6:
        numero = random.randint(1, 60)
        if numero not in palpites:
            palpites.append(numero)
            cont += 1
    cont = 0
    jogos.append(palpites)
    palpites = []
    
print(jogos)
print()
print('Fim do programa')
print()

##########

# Versão do professor:

