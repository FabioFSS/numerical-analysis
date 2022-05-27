from math import log, e, pi
from sympy import diff, integrate
from sympy.abc import x

def IntegracaoSimples(funcao, diff2, pontos):
    h = pontos[-1] - pontos[0]
    i = h*((funcao(pontos[0])+funcao(pontos[-1]))/2)

    return i

def IntegracaoMultipla(funcao, diff2, pontos):
    h = pontos[-1] - pontos[0]
    n = len(pontos)-1
    sum_pontos = sum([funcao(pontos[i]) for i in range(1, n)])
    i = h*((funcao(pontos[0])+2*sum_pontos+funcao(pontos[-1]))/(2*(n)))

    return i

def ExtrapolacaoRichards(funcao, diff2, pontos):
    i1 = IntegracaoSimples(funcao, diff2, pontos)
    i2 = IntegracaoMultipla(funcao, diff2, pontos[::2])
    i3 = IntegracaoMultipla(funcao, diff2, pontos)

    i4 = 4/3*i2 - 1/3*i1
    i5 = 4/3*i3 - 1/3*i2

    ifinal = 16/15*i5 - 1/15*i4

    return ifinal

if __name__ == '__main__':
    # faz a leitura dos dados de entrada
    with open('arquivo_entrada.txt', 'r') as file:
        lines = file.readlines()
        with open('arquivo_saida.txt', 'w') as file2:
            for i in range(0, len(lines), 3):
                funcao_string = lines[i].strip()
                funcao_string_copia = funcao_string.replace('e', 'E')
                diff2 = diff(funcao_string, (x, 2))
                funcao = lambda x: eval(funcao_string) 
                pontos = lines[i+1].strip().split()
                pontos = [float(ponto) for ponto in pontos]

                diffinter = (pontos[-1] - pontos[0])/4

                pontos = [pontos[0]+diffinter*i for i in range(5)]

                res = ExtrapolacaoRichards(funcao, diff2, pontos)

                file2.write(f'{res}\n\n')
                # file.write(f'\nerro: {err}')