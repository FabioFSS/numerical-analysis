from math import e
from matplotlib import pyplot as pt

def heun(funcoes, pontos, h, ordem):
    '''Aplica o metodo de Heun para um sistema de equações diferenciais.
    
    Parâmetros:
        funcoes (list): as funcoes que serão aplicadas
        pontos (list): a lista com os pontos que serão tomados como referência
        h (float): o intervalo entre os pontos que será calculado
        ordem (int): a ordem do ponto desejado

    Retorno:
        resultado (float or list): o resultado estimado da equação diferencial
    '''

    if len(funcoes) > 1:
        hist = []
        def func1(x, y, z): return eval(funcoes[0])
        def func2(x, y, z): return eval(funcoes[1])

        x, y, z = pontos[0][0], pontos[0][1], pontos[1][1]

        for i in range(ordem):
            k1y = func1(x, y, z)
            k1z = func2(x, y, z)

            k2y = func1(x + h, y, z + h * k1z)
            k2z = func2(x + h, y + h * k1y, z)

            y1 = y + (h/2) * (k1y + k2y)
            z1 = z + (h/2) * (k1z + k2z)

            x, y, z = x+h, y1, z1
            hist.append((x,y,z))

        return hist

    else:
        hist = []
        def func1(x, y): return eval(funcoes[0])

        x, y = pontos[0][0], pontos[0][1]

        for i in range(ordem):
            k1 = func1(x, y)
            k2 = func1(x + h, y + h * k1)

            y1 = y + (h/2) * (k1 + k2)

            x, y = x+h, y1
            hist.append((x, y))

        return hist


def grafico(solucao):
    if len(solucao[0]) == 2:
        x = [ponto[0] for ponto in solucao]
        y = [ponto[1] for ponto in solucao]
        pt.plot(y)
        pt.savefig('grafico.jpg')
        pt.show()

    else:
        x = [ponto[0] for ponto in solucao]
        y = [ponto[1] for ponto in solucao]
        z = [ponto[2] for ponto in solucao]
        pt.plot(y)
        pt.plot(z)
        pt.savefig('grafico.jpg')
        pt.show()


if __name__ == '__main__':
    with open('arquivo_entrada.txt', 'r') as file:
        # Lendo a primeira linha que contem uma ou mais funcoes
        funcao_string = file.readline().strip().split('|')
        # Lendo os pontos
        pontos = file.readline().strip().split('|')
        pontos = [ponto.split() for ponto in pontos]
        pontos = [[float(valor) for valor in ponto] for ponto in pontos]

        # Valores de h e ordem
        h = float(file.readline())
        o = int(file.readline())

        # Chama a função para resolver
        resultado = heun(funcao_string, pontos, h, o)

        # Escreve o resultado na saída
        with open('arquivo_saída.txt', 'w') as out:
            out.write(f'resultado:\n')
            for i in range(len(resultado)):
                out.write(f'it {i+1}: {resultado[i]}\n')

        grafico(resultado)