from math import log, e, pi
from sympy import diff, integrate
from sympy.abc import x


def IntegracaoSimples(funcao, diff2, a, b):
    h = b - a
    i = h*((funcao(a)+funcao(b))/2)

    # fd2x = (integrate(diff2, (x, a, b))/h)
    # err = -1/12*fd2x*h**3

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

                res = IntegracaoSimples(funcao, diff2, pontos[0], pontos[1])
                res_final = res

                file2.write(f'{res}\n\n')
            # file.write(f'\nerro: {err}')