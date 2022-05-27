import sympy as sp
from FatoracaoLU import FatoracaoLU
import matplotlib.pyplot as pt


def diferencas_finitas(funcao, r, a, b, tam) -> float:
    '''
    Aplica o método de diferencas finitas para solução de equações diferenciais.
    
    Parâmetros:
        funcao (function): f(x, y) que será aplicada
        x (float): valor de x
        y (float): valor de y
        h (float): intervalo entre os pontos que será calculado
        ordem (int): nivel de ordem desejado
        it (int): numero de iterações usado no metodo

    Retorno:
        resultado (float): resultado estimado da equação diferencial
    '''

    matriz = [[0 for i in range(tam)] for i in range(tam)]
    mr = [0 for i in range(tam)]
    funcao = sp.poly(funcao)

    coeffs = funcao.coeffs()
    matriz[0][0], matriz[0][1] = float(coeffs[1]), float(coeffs[2])
    mr[0] = r + a


    for i in range(1, tam-1):
        matriz[i][i-1] = float(coeffs[0])
        matriz[i][i] = float(coeffs[1])
        matriz[i][i+1] = float(coeffs[2])
        mr[i] = r

    matriz[-1][-1], matriz[-1][-2] = float(coeffs[1]), float(coeffs[0])
    mr[-1] = r + b

    mf  = [matriz[j] + [mr[j]] for j in range(len(matriz))]

    res = FatoracaoLU(mf)

    return res

def grafico(solucao):
    pt.plot(solucao)
    pt.savefig('grafico.jpg')
    pt.show()



if __name__ == '__main__':
    with open('arquivo_entrada.txt', 'r') as file:
        # Lendo a funcao e criando uma funcao anônima
        funcao = file.readline().strip()
        funcao = sp.poly(funcao)

        # Lendo os pontos
        r = eval(file.readline().strip())

        # Valores de h, ordem e iterações
        a, b = file.readline().strip().split()
        a, b = float(a), float(b)
        tam = int(file.readline())

        # Chama a função com os valores

        resultado = diferencas_finitas(funcao, r, a, b, tam)
        # erro = erro_diferencas_finitas(funcao_string, x, y, h, o)


        # Escreve o resultado na saída
        with open('arquivo_saída.txt', 'w') as out:
            out.write(f'resultado:\n')

            for i in range(len(resultado)):
                out.write(f'p {i+1}: {resultado[i]}\n')

        grafico(resultado)
