from math import log, e, pi
from sympy import diff, integrate
from sympy.abc import x


def Simpson38(funcao, diff4, pontos):
    h = pontos[-1] - pontos[0]
    n = len(pontos)-1
    i = h*((funcao(pontos[0])+3*funcao(pontos[1])+3*funcao(pontos[2])+funcao(pontos[-1]))/8)

    # fd2x = (integrate((diff4), (x, pontos[0], pontos[-1]))/h)
    # err = eval(str(-((h**5)/(6480))*fd2x))

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

                diffinter = (pontos[-1] - pontos[0])/3

                pontos = [pontos[0]+diffinter*i for i in range(4)]


                res = Simpson38(funcao, diff4, pontos)

                file2.write(f'{res}\n\n')
                # file.write(f'\nerro: {err}')