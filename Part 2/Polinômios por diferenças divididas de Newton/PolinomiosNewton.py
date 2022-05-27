from math import log
from sympy import Mul, simplify, factor, Add
from sympy.abc import x
import matplotlib.pyplot as mp


def CalculaBFunc(funcao, pontos):
    if len(pontos) == 1:
        return funcao(pontos[0])
    if len(pontos) == 2:
        return (funcao(pontos[1]) - funcao(pontos[0])) / \
(pontos[1] - pontos[0])
    if len(pontos) > 2:
        return (CalculaBFunc(funcao, pontos[1:]) - CalculaBFunc(funcao, pontos[:-1])) / \
            (pontos[-1] - pontos[0])

def CalculaBPontos(pontosx, pontosy):
    if len(pontosx) == 1:
        return pontosy[0]
    if len(pontosx) == 2:
        return (pontosy[1] - pontosy[0]) / \
            (pontosx[1] - pontosx[0])
    if len(pontosx) > 2:
        return (CalculaBPontos(pontosx[1:], pontosy[1:]) - CalculaBPontos(pontosx[:-1], pontosy[:-1])) / \
            (pontosx[-1] - pontosx[0])


def PolinomiosNewton(pontosx, pontosy=None, funcao=None):
    res = 0
    for i in range(len(pontosx)):
        temp_pontos = pontosx[:i+1]

        if pontosy == None:
            temp_res = CalculaBFunc(funcao, temp_pontos)
        else:
            temp_y = pontosy[:i+1]
            temp_res = CalculaBPontos(temp_pontos, temp_y)

        if len(temp_pontos) > 1:
            str_temp = 1
            for j in range(len(temp_pontos)-1):
                str_temp = simplify(factor(Mul(str_temp, eval(f'(x-{temp_pontos[j]})'))))

            temp_res =simplify(factor( Mul(temp_res, str_temp)))

        res = simplify(Add(res, temp_res))

    return simplify(factor(res))

def TestaResultados(pontosx, pontosy, polinomio):
    funcao = lambda x: eval(str(polinomio))
    res = [funcao(ponto) for ponto in pontosx]

    mp.plot(pontosx, pontosy, 'bo')
    mp.plot(pontosx, res)

    # mp.show()

    print(funcao(2.3))




if __name__ == '__main__':
    with open('arquivo_entrada.txt', 'r') as file:
        # faz a leitura dos dados de entrada para função
        # funcao_string = file.readline().strip()
        # funcao = lambda x: eval(funcao_string)
        # pontosx = file.readline().strip().split()
        # pontosx = [float(ponto) for ponto in pontosx]

        # res = PolinomiosNewton(pontosx, funcao=funcao)
        # pontosy = [funcao(ponto) for ponto in pontosx]

        # faz a leitura dos dados de entrada para pontos
        pontosx = file.readline().strip().split()
        pontosx = [float(ponto) for ponto in pontosx]

        pontosy = file.readline().strip().split()
        pontosy = [float(ponto) for ponto in pontosy]

        res = PolinomiosNewton(pontosx, pontosy)

    TestaResultados(pontosx, pontosy, res)

    with open('arquivo_saida.txt', 'w') as file:
        file.write('Polinomio: ' + str(res))