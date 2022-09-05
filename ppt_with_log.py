from random import randint as ri
from datetime import datetime


def jogar(arquivo):
    escolhas = ['Pedra', 'Papel', 'Tesoura']
    mao = int(input('=-= ESCOLHA UMA OPÇÃO =-=\n[1] - Pedra\n[2] - Papel\n[3] Tesoura\n'))
    mao_pc = ri(1, 3)
    if mao == mao_pc:
        sit = 0
    elif mao == 1:
        if mao_pc == 2:
            sit = 2
        else:
            sit = 1
    elif mao == 2:
        if mao_pc == 1:
            sit = 1
        else:
            sit = 2
    elif mao == 3:
        if mao_pc == 1:
            sit = 2
        else:
            sit = 1
    else:
        return print('Valor inválido, tente novamente.')

    if sit == 0:
        print('[RESULTADO] Empate.')
    elif sit == 1:
        print('[RESULTADO] Você venceu.')
    else:
        print('[RESULTADO] Você perdeu.')

    arquivo.write(str(datetime.now()))
    arquivo.write(f'\nEscolha humano: {escolhas[mao - 1]}')
    arquivo.write(f'\nEscolha computador: {escolhas[mao_pc - 1]}')
    arquivo.write('\n##########\n')


keep = True

while keep:
    op_jogo = int(input('1- Jogar\n2- VER PLACARES\n3- Sair\n'))
    if op_jogo == 1:
        arq = open('jogos.txt', 'a+')
        jogar(arq)
        arq.close()
    elif op_jogo == 2:
        arq = open('jogos.txt', 'r')
        print(arq.read())
        arq.close()
    elif op_jogo == 3:
        print('Saindo...')
        keep = False
