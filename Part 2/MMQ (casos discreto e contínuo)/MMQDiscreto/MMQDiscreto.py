from FatoracaoLU import FatoracaoLU
from fractions import Fraction
import matplotlib.pyplot as mp

def MMQDiscreto(pontosx, pontosy):
    # calcula os vetores u em determinado grau
    grau = 2
    u = [[x**i for x in pontosx] for i in range(grau+1)]

    # calcula os produtos escalares necessários para a matriz
    matriz = []
    b = []
    for i in range(len(u)):
        b.append(sum([pontosy[k] * u[i][k] for k in range(len(u[i]))]))

        temp = []
        for j in range(len(u)):
            temp.append(sum([u[i][k] * u[j][k] for k in range(len(u[i]))]))

        matriz.append(temp)

    # realiza o calculo do resultado da matriz utilizando Fatoracao LU
    matriz_completa = [matriz[i].copy() for i in range(len(matriz))]
    for i in range(len(matriz)): matriz_completa[i].append(b[i])
    matriz, mL, mU, mTempResultado, resultado = FatoracaoLU(matriz_completa)

    return resultado

def TestaResultados(pontosx, pontosy, polinomio):
    funcao = lambda x: eval(str(polinomio))
    res = [funcao(ponto) for ponto in pontosx]

    mp.plot(pontosx, pontosy, 'bo')
    mp.plot(pontosx, res)

    mp.show()

    print(funcao(20))


if __name__ == '__main__':
    # faz a leitura dos pontos do arquivo de entrada
    with open('arquivo_entrada.txt', 'r') as file:
        pontos = file.readlines()

        for i in range(len(pontos)):
            pontos[i] = pontos[i].split()

        pontosx = [Fraction(ponto[0]) for ponto in pontos]
        pontosy = [Fraction(ponto[1]) for ponto in pontos]
        
    res = MMQDiscreto(pontosx, pontosy)

    # faz a escrita no arquivo de saida
    with open('arquivo_saida.txt', 'w') as file:
        file.write(f'Polinomio: {float(res[0])}')
        polinomio = f'{res[0]}'
        for i in range(1, len(res)):
            file.write(f' + {float(res[i])}x**{i}')
            polinomio += f' + {res[i]}*x**{i}'

    TestaResultados(pontosx, pontosy, polinomio)