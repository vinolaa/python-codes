from operator import itemgetter


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


jogos = {
    "Vinicius": 6,
    "Julia": 3,
    "Gui": 4
}

rankingJogoDados(jogos)
