p = {1: {
        'pergunta': "Qual a idade do vinola?",
        'possibilidades': [1, 30, 20, 21, 13],
        'correto': '20'
    },
    2: {
        'pergunta': "Qual o nome do homem mais bonito do mundo?",
        'possibilidades': ["Vinicius", "Pedro", "Guilherme", "Fabio", "Henrique"],
        'correto': "Vinicius"
    },
    3: {
        'pergunta': "Treio de peitoral hoje?",
        'possibilidades': ["Sim", "Não"],
        'correto': "Sim"
    },
    4: {
        'pergunta': "O Vinola é legal?",
        'possibilidades': ["Sim", "Não"],
        'correto': "Sim"
    },
    5: {
        'pergunta': "Pergunta 5?",
        'possibilidades': [1, 2, 3, 4, 5],
        'correto': '5'
    }
}


def jogar(banco):
    pontos = 0
    print("\nVESTIBULAR\n=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    for i, j in banco.items():
        print(f"Pergunta número {i}: ", j["pergunta"])
        print(f"Alternativas: ", j["possibilidades"])
        resposta = input('Digite sua respota: ')
        if resposta == j["correto"]:
            pontos += 1
            print('Resposta correta!')
            print(pontos)
        else:
            print('Resposta incorreta!')
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(f'Parabéns! Você fechou o vestibular com um total de {pontos}/{len(banco)} pontos.')


jogar(p)
