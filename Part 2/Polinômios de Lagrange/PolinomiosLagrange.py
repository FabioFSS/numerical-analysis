from math import log
from sympy import Mul, simplify, factor
from sympy.abc import x
import matplotlib.pyplot as mp

def PolinomiosLagrange(pontosx, pontosy=None, funcao=None):
    res = 0
    for i in range(len(pontosx)):
        novo_pontos = [ponto for ponto in pontosx if ponto != pontosx[i]]
        
        num_string = 1
        for j in range(len(novo_pontos)):
            num_string = Mul(num_string, eval(f'(x-{novo_pontos[j]})'))


        den = 1
        for j in range(len(novo_pontos)):
          den *= pontosx[i] - novo_pontos[j]

        l = Mul(eval(str(1/den)), num_string)

        if funcao == None:
            res += simplify(factor(Mul(pontosy[i], l)))
        else:
            res += simplify(factor(Mul(funcao(pontosx[i]), l)))

    return simplify(factor(res))

def TestaResultados(pontosx, pontosy, polinomio):
    funcao = lambda x: eval(str(polinomio))
    res = [funcao(ponto) for ponto in pontosx]

    mp.plot(pontosx, pontosy, 'bo')
    mp.plot(pontosx, res)

    mp.show()

    print(str(polinomio).replace('x', '1730'))
    print(funcao(1730))
    print(str(polinomio).replace('x', '3200'))
    print(funcao(3200))
    print(str(polinomio).replace('x', '2.3'))
    print(funcao(2.3))



if __name__ == '__main__':
    with open('arquivo_entrada.txt', 'r') as file:
        # faz a leitura dos dados de entrada para função
        # funcao_string = file.readline().strip()
        # funcao = lambda x: eval(funcao_string)
        # pontosx = file.readline().strip().split()
        # pontosx = [float(ponto) for ponto in pontosx]

        # res = PolinomiosLagrange(pontosx, funcao=funcao)

        # faz a leitura dos dados de entrada para pontos
        pontosx = file.readline().strip().split()
        pontosx = [float(ponto) for ponto in pontosx]

        pontosy = file.readline().strip().split()
        pontosy = [float(ponto) for ponto in pontosy]

        res = PolinomiosLagrange(pontosx, pontosy)

    TestaResultados(pontosx, pontosy, res)

    with open('arquivo_saida.txt', 'w') as file:
        file.write('Polinomio: '+str(res))