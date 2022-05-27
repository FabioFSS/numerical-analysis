from math import log, e, pi
from sympy import diff, integrate
from sympy.abc import x


def Simpson13(funcao, diff4, pontos):
    h = pontos[-1] - pontos[0]
    n = len(pontos)-1
    i = h*((funcao(pontos[0])+4*funcao(pontos[1])+funcao(pontos[-1]))/6)

    # fd2x = (integrate((diff4), (x, pontos[0], pontos[-1]))/h)
    # err = eval(-((h**5)/(2880))*fd2x)

    return i


def Simpson13Multipla(funcao, diff4, pontos):
    h = pontos[-1] - pontos[0]
    n = len(pontos)-1
    sum_impar = sum([funcao(pontos[i]) for i in range(1, n, 2)])
    sum_par = sum([funcao(pontos[i]) for i in range(2, n-1, 2)])
    i = h*((funcao(pontos[0])+4*sum_impar+2*sum_par+funcao(pontos[-1]))/(3*n))

    # fd2x = (integrate((diff4), (x, pontos[0], pontos[-1]))/h)
    # err = eval(str(-((h**5)/(180*(n**4)))*fd2x))

    return i


if __name__ == '__main__':
    # faz a leitura dos dados de entrada
    with open('arquivo_entrada.txt', 'r') as file:
        lines = file.readlines()
        with open('arquivo_saida.txt', 'w') as file2:
            for i in range(0, len(lines), 3):
                funcao_string = lines[i].strip()
                funcao_string_copia = funcao_string.replace('e', 'E')
                diff4 = diff(funcao_string, (x, 4))
                funcao = lambda x: eval(funcao_string) 
                pontos = lines[i+1].strip().split()
                pontos = [float(ponto) for ponto in pontos]

                diffinter = (pontos[-1] - pontos[0])/4

                pontos = [pontos[0]+diffinter*i for i in range(5)]

                res = Simpson13Multipla(funcao, diff4, pontos)

                file2.write(f'{res}\n\n')
                # file.write(f'\nerro: {err}')