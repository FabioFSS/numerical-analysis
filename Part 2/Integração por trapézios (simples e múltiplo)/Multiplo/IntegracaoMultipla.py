from math import log, e, pi
from sympy import diff, integrate
from sympy.abc import x


def IntegracaoMultipla(funcao, diff2, pontos):
    h = pontos[-1] - pontos[0]
    n = len(pontos)-1
    sum_pontos = sum([funcao(pontos[i]) for i in range(1, n)])
    i = h*((funcao(pontos[0])+2*sum_pontos+funcao(pontos[-1]))/(2*(n)))

    # fd2x = sum([(integrate(diff2, (x, pontos[i], pontos[i+1]))/h) for i in range(n)])
    # err = -((h**3)/(12*(n**2)))*fd2x

    return i




if __name__ == '__main__':
    # faz a leitura dos dados de entrada
    with open('arquivo_entrada.txt', 'r') as file:
        with open('arquivo_saida.txt', 'w') as file2:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                funcao_string = lines[i].strip()
                interval = lines[i+1].split()
                funcao_string_copia = funcao_string.replace('e', 'E')
                diff1 = diff(funcao_string_copia)
                diff2 = diff(diff1)
                funcao = lambda x: eval(funcao_string) 
                pontos = [float(ponto) for ponto in interval]

            
                diffinter = (pontos[-1] - pontos[0]) / 4

                pontos = [pontos[0]+diffinter*i for i in range(5)]

                res = IntegracaoMultipla(funcao, diff2, pontos)

                file2.write(f'{res}\n\n')
                # file.write(f'\nerro: {err}')