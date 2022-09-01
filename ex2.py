from operator import itemgetter

def ficha_funcionarios(dicionario):
    for i, j in dicionario.items():
        print(f'Funcionario: {i} | Salario: {j}')
    lista = list(dicionario.items())
    ordenada = sorted(lista, key=itemgetter(1), reverse=False)
    print(f'O funcionário {ordenada[0][0]} tem o menor salário, no valor de {ordenada[0][1]}')


funcionarios = {
    "Vini": 3000,
    "Julia": 600,
    "Gui": 1000
}

ficha_funcionarios(funcionarios)
