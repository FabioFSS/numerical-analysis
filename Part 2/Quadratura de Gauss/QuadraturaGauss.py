from math import log, e, pi
from sympy import diff, integrate
from sympy.abc import x

def QuadraturaGauss(funcao, pontos):
    pesos = [[1], [0.5555556, 0.8888889],
            [0.3478548, 0.6521452], [0.2369269, 0.4786287, 0.5688889],
            [0.1713245, 0.3607616, 0.4679139]]

    raizes = [[-0.577350269], [-0.774596669, 0],
            [-0.861136312, -0.339981044], [-0.906179846, -0.538469310, 0],
            [-0.932469514, -0.661209386, -0.238619186]]

    peso = pesos[len(pontos)-2]
    raiz = raizes[len(pontos)-2]

    a = pontos[0]
    b = pontos[-1]    

    nx = f'((({b} + {a}) + ({b} - {a})*x) / 2)'
    ndx = f'(({b} - {a})/2)'
    funcao_nova = funcao.replace('x', nx)
    funcao_nova = f'({funcao_nova}) * {ndx}'

    res = 0
    for i in range(len(peso)):
        if raiz[i] == 0:
            res += peso[i]*eval(funcao_nova.replace('x', str(raiz[i])))
        else:
            res += peso[i]*eval(funcao_nova.replace('x', str(raiz[i])))
            res += peso[i]*eval(funcao_nova.replace('x', str(-raiz[i])))

    return res


if __name__ == '__main__':
    # faz a leitura dos dados de entrada
    with open('arquivo_entrada.txt', 'r') as file:
        lines = file.readlines()
        with open('arquivo_saida.txt', 'w') as file2:
            for i in range(0, len(lines), 3):
                funcao_string = lines[i].strip()
                funcao = lambda x: eval(funcao_string) 
                pontos = lines[i+1].strip().split()
                pontos = [float(ponto) for ponto in pontos]

                diffinter = (pontos[-1] - pontos[0])/4

                pontos = [pontos[0]+diffinter*i for i in range(5)]

                res = QuadraturaGauss(funcao_string, pontos)

                file2.write(f'{res}\n\n')