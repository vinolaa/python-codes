import random
from operator import itemgetter


def inserir_jogadores(dic):
    qtd = int(input("Insira a quantidade de jogadores (até 4): "))
    if qtd > 4:
        print("Máximo de 4 jogadores!")
        return
    else:
        for i in range(qtd):
            nome = input('Insira o nome do jogador: ')
            dado = random.randint(1, 6)
            dic[nome] = dado


def rankingJogoDados(jogadas):
    aux = 1
    print('VALORES SORTEADOS:')
    lista = list(jogadas.items())
    for i, j in lista:
        print(f'{i} tirou {j}')
    print('RANKING DOS JOGADORES:')
    ordenada = sorted(lista, key=itemgetter(1), reverse=True)
    for i, j in ordenada:
        print(f'{aux}º lugar: {i} com {j}')
        aux += 1


jogos = {}

inserir_jogadores(jogos)
rankingJogoDados(jogos)
