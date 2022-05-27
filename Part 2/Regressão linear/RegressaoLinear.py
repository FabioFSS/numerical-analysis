from fractions import Fraction
import matplotlib
import matplotlib.pyplot as mp


def RegressaoLinear(pontosx, pontosy):
    # numero de pontos
    tam = len(pontosx)

    # realiza os calculos de somatório e medias
    somaxy = sum([pontosx[i]*pontosy[i] for i in range(len(pontosx))])
    somaxq = sum([x**2 for x in pontosx])
    somayq = sum([y**2 for y in pontosy])
    somax = sum(pontosx)
    somay = sum(pontosy)
    xmed = somax / tam
    ymed = somay / tam

    # calcula os valores de a0 e a1
    a1 = (tam * somaxy - somax * somay) / (tam * somaxq - somax**2)
    a0 = ymed - a1 * xmed

    # calcula o valor de r (coeficiente de determinação)
    r = (tam * somaxy - somax * somay) / ((tam * somaxq - somax**2)**(1/2) * (tam * somayq - somay**2)**(1/2))

    return a0, a1, r

def TestaResultados(pontosx, pontosy, a0, a1):
    res = [a0 + a1*ponto for ponto in pontosx]
    mp.plot(pontosx, pontosy, 'bo')
    mp.plot(pontosx, res)

    mp.show()


if __name__ == '__main__':
    # faz a leitura dos pontos do arquivo de entrada
    with open('arquivo_entrada.txt', 'r') as file:
        pontos = file.readlines()

        for i in range(len(pontos)):
            pontos[i] = pontos[i].split()

        pontosx = [float(ponto[0]) for ponto in pontos]
        pontosy = [float(ponto[1]) for ponto in pontos]
        
    a0, a1, r = RegressaoLinear(pontosx, pontosy)

    TestaResultados(pontosx, pontosy, a0, a1)

    # faz a escrita dos dados na saída
    with open('arquivo_saida.txt', 'w') as file:
        file.write(f'reta: {a0} + {a1}x\n')
        file.write(f'coeficiente de determinacao: {r}')